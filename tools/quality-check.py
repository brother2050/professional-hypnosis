#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全书质量检查工具（对应 references/编辑规范.md §6"四项检查"）

用法：
    python3 tools/quality-check.py          # 跑全部检查
    python3 tools/quality-check.py --quick  # 只跑链接/锚点/围栏/标点

检查项：
  1. 坏链（相对文件路径不存在）
  2. 锚点（#锚点 在目标文件中不存在）
  3. 代码围栏平衡
  4. 中文语境半角标点残留
  5. 章号-标题错位引用（第N章（提示）与真实章名不符）
  6. 附录字母引用（指向不存在的附录）
  7. 术语变体（催眠易感性/可催眠性/催眠后暗示）
  8. 章节模板四件套（摘要/延伸阅读/思考题/术语表）
退出码：0=全绿，1=有问题（可接入 CI）。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON = {1:'导论|定义|学科|边界',2:'历史|演进|流派',3:'神经科学|脑',4:'理论|模型',5:'意识|暗示|感受',6:'诱导|导入',7:'深化',8:'暗示|设计',9:'唤醒|后催眠',10:'自我催眠|训练',
         11:'团体',12:'镇痛|疼痛',13:'焦虑|恐惧|创伤',14:'整合',15:'医学|产科|手术|IBS',16:'儿童|青少年',17:'成瘾|习惯|戒',18:'新进展|进展',
         19:'影像',20:'人工智能|虚拟现实|AI|VR',21:'跨文化',22:'伦理'}
BANNED_TERMS = {'催眠易感性': '催眠感受性', '可催眠性': '催眠感受性', '催眠后暗示': '后催眠暗示'}
problems = []


def files():
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT)
        if rel.split(os.sep)[0] in ('.git', '.openclaw', 'tools'):
            continue
        for f in sorted(fn):
            if f.endswith('.md'):
                yield os.path.join(dp, f)


def anchor_of(text):
    t = text.strip().lower()
    t = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', t)
    return t.replace(' ', '-')


def check_links_anchors_fences_punct():
    for p in files():
        rel = os.path.relpath(p, ROOT)
        text = open(p, encoding='utf-8').read()
        lines = text.split('\n')
        counts, anchors = {}, set()
        for l in lines:
            m = re.match(r'^(#{1,6})\s+(.*)', l)
            if m:
                a = anchor_of(m.group(2))
                n = counts.get(a, 0); counts[a] = n + 1
                anchors.add(a if n == 0 else f'{a}-{n}')
        if sum(1 for l in lines if l.strip().startswith('```')) % 2:
            problems.append(f'[围栏] {rel}: 代码围栏不成对')
        infence = False
        for i, l in enumerate(lines, 1):
            if l.strip().startswith('```'):
                infence = not infence
                continue
            for m in re.finditer(r'\]\(([^)]+)\)', l):
                t = m.group(1).strip()
                if t.startswith(('http', 'mailto', '#')):
                    continue
                pp, _, an = t.partition('#')
                if pp:
                    tp = os.path.normpath(os.path.join(os.path.dirname(p), pp))
                    if not os.path.exists(tp):
                        problems.append(f'[坏链] {rel}:{i} -> {t}')
                    elif an:
                        src = open(tp, encoding='utf-8').read()
                        c2, a2 = {}, set()
                        for l2 in src.split('\n'):
                            mm = re.match(r'^(#{1,6})\s+(.*)', l2)
                            if mm:
                                a = anchor_of(mm.group(2)); n = c2.get(a, 0); c2[a] = n + 1
                                a2.add(a if n == 0 else f'{a}-{n}')
                        if an not in a2:
                            problems.append(f'[锚点] {rel}:{i} {t}')
                elif an and an not in anchors:
                    problems.append(f'[锚点] {rel}:{i} #{an}')
            if not infence:
                for m in re.finditer(r'[\u4e00-\u9fff“”）」][,;:?!](?![0-9A-Za-z/.）\]}])', l):
                    problems.append(f'[标点] {rel}:{i} 半角标点混入中文')


def check_refs():
    letters = set()
    for f in os.listdir(os.path.join(ROOT, 'appendix')):
        if f.endswith('.md'):
            m = re.search(r'^# 附录([A-Z]{1,2})：', open(os.path.join(ROOT, 'appendix', f), encoding='utf-8').read(), re.M)
            if m:
                letters.add(m.group(1))
    chap_hint = re.compile(r'第\s?([0-9]{1,2})\s?章[（(]([^）)]{2,14})[）)]')
    app_ref = re.compile(r'附录\s?([A-Z]{1,2})(?![A-Za-z])')
    for p in files():
        rel = os.path.relpath(p, ROOT)
        if rel.startswith('references'):
            continue
        for i, l in enumerate(open(p, encoding='utf-8'), 1):
            for m in chap_hint.finditer(l):
                n, hint = int(m.group(1)), m.group(2)
                if re.search(r'[，、；：⭐⚠️→（(]', hint):
                    continue  # 注释性括注（非章名），跳过
                if n in CANON and not re.search(CANON[n], hint):
                    problems.append(f'[章号] {rel}:{i} 第{n}章（{hint}）与「{CANON[n]}」不符')
            for m in app_ref.finditer(l):
                if m.group(1) not in letters and m.group(1) != 'C':
                    problems.append(f'[附录] {rel}:{i} 附录{m.group(1)} 不存在')


def check_terms():
    for p in files():
        rel = os.path.relpath(p, ROOT)
        if rel == os.path.join('references', '编辑规范.md'):
            continue  # 规范文件本身以禁用词为例
        t = open(p, encoding='utf-8').read()
        for bad, good in BANNED_TERMS.items():
            n = t.count(bad)
            if n:
                problems.append(f'[术语] {rel}: "{bad}" x{n}（应为「{good}」）')


def check_stats():
    """README 内容统计 vs 实测：防统计漂移"""
    import json
    readme = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read()
    n_md = 0
    cjk = 0
    n_app = len([f for f in os.listdir(os.path.join(ROOT, 'appendix')) if f.endswith('.md')])
    for dp, dn, fn in os.walk(ROOT):
        rel_parts = os.path.relpath(dp, ROOT).split(os.sep)
        if any(x in rel_parts for x in ('.git', '.openclaw', 'tools', '.github')):
            continue
        for f in fn:
            if f.endswith('.md'):
                n_md += 1
                cjk += sum(1 for ch in open(os.path.join(dp, f), encoding='utf-8').read() if '\u4e00' <= ch <= '\u9fff')
    m = re.search(r'\| 总文件数 \| (\d+) 个 \|', readme)
    if m and int(m.group(1)) != n_md:
        problems.append(f'[统计] README 总文件数 {m.group(1)} ≠ 实测 {n_md}')
    m = re.search(r'\| 总字数 \| ~(\d+) 万字 \|', readme)
    if m and abs(int(m.group(1)) - round(cjk / 10000)) > 1:
        problems.append(f'[统计] README 总字数 {m.group(1)}万 ≠ 实测 {round(cjk/10000)}万')
    m = re.search(r'\| 附录 \| (\d+) 个 \|', readme)
    if m and int(m.group(1)) != n_app:
        problems.append(f'[统计] README 附录 {m.group(1)} ≠ 实测 {n_app}')


def check_template():
    d = os.path.join(ROOT, 'chapters')
    for f in sorted(os.listdir(d)):
        t = open(os.path.join(d, f), encoding='utf-8').read()
        miss = []
        if '核心内容摘要' not in t: miss.append('摘要')
        if '延伸阅读' not in t and '参考文献' not in t: miss.append('延伸阅读')
        if '思考' not in t: miss.append('思考题')
        if '术语' not in t: miss.append('术语表')
        if miss:
            problems.append(f'[模板] chapters/{f}: 缺 {",".join(miss)}')


def main():
    quick = '--quick' in sys.argv
    check_links_anchors_fences_punct()
    if not quick:
        check_refs()
        check_terms()
        check_template()
        check_stats()
    if problems:
        print(f'❌ 发现 {len(problems)} 项问题：')
        for x in problems:
            print('  ', x)
        sys.exit(1)
    print('✅ 全部检查通过（链接/锚点/围栏/标点' + ('' if quick else '/引用/术语/模板') + '）')


if __name__ == '__main__':
    main()
