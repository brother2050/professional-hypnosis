# LLM/AI 使用指引（token 与超时预算）

> **📌 本篇摘要**
> - **这是什么**：给 LLM 应用、RAG 检索、Agent 流水线使用本书的操作手册——阅读路径、场景路由、token 预算、流水线规则一次说清。
> - **适用场景**：把本书接入 AI 助手；做批量摘要；搭检索问答；为模型规划阅读顺序。
> - **关键结论**：先读文件头部摘要再决定是否展开；单次调用控制在约 8K token；超过 32KB 的文件按二级节分块；超时重试只补断点小节。
> - **去哪里深入**：文件地图见 [SUMMARY.md](../SUMMARY.md)；写作与修订规则见 [编辑规范](编辑规范.md)；安全红线见 [DISCLAIMER](../DISCLAIMER.md)。
> - **场景关键词**：LLM｜token 预算｜RAG 分块｜检索路由｜阅读路径｜超时重试

> **🔗 前后衔接**：前置：无（本篇自足，可直接照做）；本篇解决：机器怎么高效、安全地读这本书；深入：[编辑规范](编辑规范.md) 第 7 节（LLM 工程化条目）。

**路径写法约定**：下文路径一律相对仓库根（如 `chapters/12-pain-management.md`）；“小节”用文件内编号（如 `12.7`、`AH.4`、`脚本5`）。路由表与预算表可整表交给程序解析。

---

## 一、按用途的阅读路径

先给结论：四条路线，按任务挑一条从上往下读。每个文件先读前 30 行摘要块，命中目标小节再展开正文。

### 路线 1：新手安全先行（任何练习、任何个案之前）

1. `DISCLAIMER.md`（安全底线全文）
2. `CORE-SUMMARY.md`（一、二、三、九、十五）
3. `chapters/01-introduction.md`（什么是催眠、边界在哪）
4. `chapters/22-ethics-legal.md`（22.1 伦理框架、22.2 知情同意）
5. `appendix/g-safety-manual.md`（高风险技术与不良反应处置）
6. `appendix/o-study-guide.md`（后续学习路线）

**完成判据**：能原样复述三条安全红线——不恢复记忆、不替代医疗、无知情同意不动手。

### 路线 2：临床速用（近期就要接个案）

1. `ACTION-GUIDE.md`（速用流程）
2. `appendix/m-clinical-quickref.md`（流程、脚本、禁忌速查）
3. `appendix/treatment-protocols.md`（按问题取协议模板）
4. `scripts/催眠脚本库.md`（取可照读脚本）
5. `chapters/06-induction-techniques.md` → `chapters/07-deepening.md` → `chapters/08-suggestion-design.md` → `chapters/09-emergence-post-hypnotic.md`（五步操作细节）
6. 按方向选读：`chapters/12-pain-management.md`（疼痛）/`chapters/13-anxiety-trauma.md`（焦虑与创伤）/`chapters/15-medical-applications.md`（医学）/`chapters/16-pediatric-hypnosis.md`（儿童）/`chapters/17-addiction-habits.md`（成瘾与习惯）
7. `appendix/i-failure-difficulties.md`（效果不好怎么办）

**完成判据**：能排出“评估-诱导-深化-暗示-唤醒”五步方案，并写清知情同意要点与失败分支。

### 路线 3：教学培训（备课、带学员）

1. `TEACHING-GUIDE.md`（课时方案、考核标准）
2. `appendix/o-study-guide.md`（五阶段路线与优先级标注）
3. `CORE-SUMMARY.md`（课堂讲义骨架）
4. `chapters/00-theory-evolution.md` 至 `chapters/05-consciousness-suggestibility.md`（理论底座）
5. `exercises/训练练习册.md`（22 章配套练习）
6. `references/练习题参考答案.md`（答题要点）
7. `case-studies/实战案例集.md`（课堂讨论素材）

**完成判据**：每个课时都有对应练习题，且答案要点能对上。

### 路线 4：研究深读（查证据、写综述）

1. `references/verification-status.md`（每条引文的核实状态）
2. `references/core-papers.md`（条目版参考文献与主题推荐）
3. `appendix/n-research-methods.md`（研究设计与证据分级）
4. `chapters/03-neuroscience.md`、`chapters/04-psychological-models.md`、`chapters/18-recent-advances.md`、`chapters/19-neuroimaging.md`
5. `appendix/f-research-overview.md`（进展速览）
6. `appendix/p-research-corrections.md`（被推翻的结论，防踩坑）
7. 按主题进专题附录：`appendix/aj-pain-science.md`（疼痛）、`appendix/ar-trauma-neurobiology.md`（创伤）、`appendix/as-emotion-regulation.md`（情绪）等

**完成判据**：引用前能说出该条目的核实状态，并区分“已验证”与“需核实”。

---

## 二、场景路由表（场景关键词 → 文件+小节）

用户问题命中左列关键词，先读中列小节；不够再看右列。此表可直接喂给检索路由程序。

| 场景关键词 | 首选文件+小节 | 补充 |
|---|---|---|
| 失眠、入睡困难、睡眠日记 | `scripts/催眠脚本库.md` 脚本5：睡眠改善；`appendix/ah-sleep-medicine.md` AH.3 | `appendix/treatment-protocols.md` 失眠催眠治疗协议 |
| 夜醒、睡眠维持困难 | `scripts/催眠脚本库.md` 脚本9：睡眠改善与深度休息；`appendix/ah-sleep-medicine.md` AH.4 | `appendix/m-clinical-quickref.md` 2.3 睡眠改善速查 |
| 睡眠卫生、作息调整 | `appendix/ah-sleep-medicine.md` AH.5 | `chapters/10-self-hypnosis.md` 10.3 |
| 慢性疼痛、镇痛 | `chapters/12-pain-management.md` 12.4、12.7 | `appendix/aj-pain-science.md` AJ.2、AJ.6；`scripts/催眠脚本库.md` 脚本3 |
| 急性疼痛、操作性疼痛 | `chapters/12-pain-management.md` 12.3 | `chapters/15-medical-applications.md` 15.1 |
| 术前焦虑、手术 | `chapters/15-medical-applications.md` 15.1、15.14 | `appendix/treatment-protocols.md` 通用治疗协议模板 |
| 肠易激综合征、腹胀腹痛 | `chapters/15-medical-applications.md` 15.2 | `appendix/av-gut-brain-axis.md` 三、六（肠道定向方案含脚本） |
| 癌症支持、放化疗不适 | `chapters/15-medical-applications.md` 15.3 | `appendix/am-complex-cases.md` |
| 产科、分娩、孕产 | `chapters/15-medical-applications.md` 15.4 | `DISCLAIMER.md` 七（孕妇） |
| 牙科、口腔操作 | `chapters/15-medical-applications.md` 15.6 | `appendix/m-clinical-quickref.md` 二 |
| 焦虑、紧张、放松训练 | `chapters/13-anxiety-trauma.md` 13.1、13.2、13.6 | `scripts/催眠脚本库.md` 脚本1、脚本7；`appendix/as-emotion-regulation.md` |
| 恐惧症、害怕、回避 | `chapters/13-anxiety-trauma.md` 13.3 | `scripts/催眠脚本库.md` 脚本14：恐惧释放脚本 |
| 惊恐发作 | `chapters/13-anxiety-trauma.md` 13.5、13.8 | `appendix/m-clinical-quickref.md` 七 |
| 创伤、PTSD、稳定化 | `chapters/13-anxiety-trauma.md` 13.4、13.7 | `appendix/an-trauma-informed.md` 三、四；`scripts/催眠脚本库.md` 脚本10 |
| 噩梦、闯入性记忆 | `appendix/an-trauma-informed.md` 五 | `appendix/ar-trauma-neurobiology.md` |
| 戒烟 | `chapters/17-addiction-habits.md` 17.2、17.12 | `scripts/催眠脚本库.md` 脚本13 |
| 减重、情绪性进食 | `chapters/17-addiction-habits.md` 17.4 | `scripts/催眠脚本库.md` 脚本6、脚本11 |
| 咬指甲、抖腿等小动作 | `chapters/16-pediatric-hypnosis.md` 16.3 | `chapters/17-addiction-habits.md` 17.5（习惯改变） |
| 儿童、故事、游戏化 | `chapters/16-pediatric-hypnosis.md` 16.1、16.2、16.12 | `appendix/m-clinical-quickref.md` 九 |
| 青少年、学业压力 | `chapters/16-pediatric-hypnosis.md` 16.4、16.13 | `DISCLAIMER.md` 七（青少年） |
| 考试焦虑 | `scripts/催眠脚本库.md` 脚本15：考试焦虑脚本 | `chapters/16-pediatric-hypnosis.md` 16.15 |
| 演讲焦虑、当众发言 | `appendix/y-organizational.md` 一之 3（演讲和沟通能力提升） | `chapters/09-emergence-post-hypnotic.md` 9.6 脚本二；`appendix/m-clinical-quickref.md` 2.4 |
| 自信心、自我效能 | `scripts/催眠脚本库.md` 脚本4、脚本8 | `chapters/10-self-hypnosis.md` 10.3 |
| 自我催眠、日常练习 | `chapters/10-self-hypnosis.md` 10.2、10.12 | `appendix/g-safety-manual.md` 四；`scripts/催眠脚本库.md` 脚本1 |
| 诱导方法、怎么导入 | `chapters/06-induction-techniques.md` 6.1、6.2 | `appendix/m-clinical-quickref.md` 三（技术选择速查表） |
| 深化、加深、走神 | `chapters/07-deepening.md` | `appendix/ak-advanced-techniques.md` |
| 暗示设计、话术改写 | `chapters/08-suggestion-design.md` 8.1、8.9、8.13 | `scripts/催眠脚本库.md` 使用指南 |
| 唤醒、催不醒怎么办 | `chapters/09-emergence-post-hypnotic.md` 9.1 | `appendix/m-clinical-quickref.md` 七 |
| 后催眠暗示、触发器 | `chapters/09-emergence-post-hypnotic.md` 9.2、9.10 | `chapters/08-suggestion-design.md` 8.3 |
| 感受性测评、量表 | `appendix/a-scales.md` 一、四 | `appendix/a-scales.md` 快速筛查量表（10 题版）；`chapters/05-consciousness-suggestibility.md` 5.3 |
| 深度评估、分级 | `appendix/m-clinical-quickref.md` 四 | `chapters/07-deepening.md` |
| 禁忌症、能不能做 | `appendix/m-clinical-quickref.md` 八；`DISCLAIMER.md` 二 | `appendix/g-safety-manual.md` |
| 不良反应、应急处理 | `appendix/g-safety-manual.md` 五、六 | `DISCLAIMER.md` 二（紧急情况处理） |
| 年龄退行、恢复记忆、司法取证 | `appendix/g-safety-manual.md` 一；`chapters/22-ethics-legal.md` 22.5 | `CORE-SUMMARY.md` 三、九（行业红线） |
| 远程催眠、视频催眠 | `DISCLAIMER.md` 六 | `appendix/be-telehealth-digital.md` |
| AI 工具、App、数字催眠 | `DISCLAIMER.md` 五 | `appendix/g-safety-manual.md` 二；`chapters/20-ai-vr.md` |
| VR、虚拟现实 | `chapters/20-ai-vr.md` | `appendix/be-telehealth-digital.md` |
| 团体催眠、工作坊 | `chapters/11-group-stage.md` | `appendix/treatment-protocols.md` 团体催眠治疗协议 |
| 老年、痴呆、照护 | `appendix/ai-aging-dementia.md` 二、三 | `DISCLAIMER.md` 七（老年人） |
| 运动表现、比赛 | `appendix/x-sports-performance.md` 二、六 | `appendix/treatment-protocols.md` 运动表现提升协议 |
| 中国本土化、文化差异 | `appendix/k-chinese-context.md` 三、八 | `chapters/21-cross-cultural.md` |
| 效果不好、失败案例 | `appendix/i-failure-difficulties.md` 三、五 | `case-studies/实战案例集.md` |
| 知情同意、记录表单 | `appendix/practical-tools.md` 知情同意书模板、治疗记录模板 | `chapters/22-ethics-legal.md` 22.2 |
| 培训、认证、督导 | `appendix/d-certifications.md`;`appendix/e-supervision.md` | `chapters/22-ethics-legal.md` 22.4、22.7 |
| 研究方法、证据分级 | `appendix/n-research-methods.md` 四、五 | `CORE-SUMMARY.md` 十六 |
| 文献核实、识别编造 | `references/verification-status.md` | `references/core-papers.md` 七 |
| 惊恐发作、惊恐、急性焦虑 | `scripts/场景脚本库.md` 脚本18：焦虑与惊恐急性安抚；`case-studies/场景案例集.md` 案例22 | `ACTION-GUIDE.md` 4.9 惊恐发作急性场景卡 |
| 公开演讲、汇报、上台紧张 | `scripts/场景脚本库.md` 脚本19：公开演讲与汇报表现；`case-studies/场景案例集.md` 案例23 | `ACTION-GUIDE.md` 4.8 场景卡；`EXAMPLES.md` 暗示句库4.4 |
| 分娩、陪产、产科镇痛 | `scripts/场景脚本库.md` 脚本25：分娩与产科镇痛 | `ACTION-GUIDE.md` 4.12 场景卡（含医疗配合边界） |
| 哀伤、丧亲、失落 | `scripts/场景脚本库.md` 脚本22：哀伤陪伴与资源唤回；`case-studies/场景案例集.md` 案例25 | `ACTION-GUIDE.md` 4.13 场景卡 |
| 儿童、写作业、专注、家长 | `scripts/场景脚本库.md` 脚本23：儿童专注与学习（含家长引导词）；`case-studies/场景案例集.md` 案例26 | `ACTION-GUIDE.md` 4.6 场景卡 |
| 拖延、倦怠、行动力 | `scripts/场景脚本库.md` 脚本28：拖延改善与行动启动；`case-studies/场景案例集.md` 案例24 | `exercises/训练练习册.md` 场景模拟训练包 |
| 拒学、厌学、青少年压力 | `case-studies/场景案例集.md` 案例28；`scripts/场景脚本库.md` 脚本24：青少年压力与自信 | `ACTION-GUIDE.md` 4.11 场景卡 |
| 慢性病、糖尿病、带病生活 | `scripts/场景脚本库.md` 脚本21：慢性病适应与带病生活；`case-studies/场景案例集.md` 案例27 | `ACTION-GUIDE.md` 4.14 场景卡 |
| 自我催眠教学、教来访者 | `scripts/场景脚本库.md` 脚本29：自我催眠一日流程 | `ACTION-GUIDE.md` 5. 自我催眠五步 |
| 团体、工作坊、小聚引导 | `scripts/场景脚本库.md` 脚本30：团体工作坊引导词 | `ACTION-GUIDE.md` 4.7 团体场景卡 |
| 唤醒困难、叫不醒 | `scripts/场景脚本库.md` 脚本31：唤醒困难接续处理脚本 | `ACTION-GUIDE.md` 6. 异常与应急 |
| 催眠前谈话、破除误解、知情同意 | `scripts/场景脚本库.md` 脚本32：催眠前谈话与期望建立；`EXAMPLES.md` §10 催眠前谈话 | `ACTION-GUIDE.md` 0. 零基础最小知识包 |
| 愤怒、情绪失控、降温 | `scripts/场景脚本库.md` 脚本27：愤怒管理与情绪降温 | `EXAMPLES.md` 8. 异常处理对话 |

---

## 三、per-file token 预算表

**估算口径（先说怎么算的）：**

- 字节数用 `wc -c` 于 2026-10-23 全书本轮优化完成后实测，与全书 v1.3.4 同步。
- 中文按 1 个汉字 ≈ 1.5 token 估算；1 个汉字在 UTF-8 里占 3 字节，所以纯中文文件 **token ≈ 字节 ÷ 2**。
- 含英文文献条目、代码块、长表格的文件更省 token，按 **字节 ÷ 2.5-3** 折算更保险；上表的“≈token”一律用 ÷ 2 的保守值。
- 读入建议三档：**一次性读入**（≤16KB，约 8K token 以内）；**可一次读入，紧时分 2 块**（16-32KB）；**分块（按二级节）**（>32KB）。
- 分块统一按二级节切：章节按 `## X.Y`，附录按 `## X.N` 或 `## 一、`，脚本库按 `## 脚本N`，每块控制在 4K token 以内。

### 3.1 导读与总览（先读这批，最划算）

| 文件 | 字节 | ≈token | 读入建议 |
|---|---:|---:|---|
| `README.md` | 32,174 | ≈16,100 | 分块（按二级节） |
| `SUMMARY.md` | 8,078 | ≈4,000 | 一次性读入 |
| `PREFACE.md` | 3,399 | ≈1,700 | 一次性读入 |
| `DISCLAIMER.md` | 12,543 | ≈6,300 | 一次性读入 |
| `CORE-SUMMARY.md` | 19,758 | ≈9,900 | 可一次读入，紧时分2块 |
| `ACTION-GUIDE.md` | 67,787 | ≈33,900 | 分块（按二级节） |
| `EXAMPLES.md` | 50,782 | ≈25,400 | 分块（按二级节） |
| `DEPTH-GUIDE.md` | 13,251 | ≈6,600 | 一次性读入 |
| `TEACHING-GUIDE.md` | 14,769 | ≈7,400 | 一次性读入 |

### 3.2 正文 23 章

| 文件 | 字节 | ≈token | 读入建议 |
|---|---:|---:|---|
| `chapters/00-theory-evolution.md` | 48,292 | ≈24,100 | 分块（按二级节） |
| `chapters/01-introduction.md` | 40,622 | ≈20,300 | 分块（按二级节） |
| `chapters/02-history.md` | 28,918 | ≈14,500 | 可一次读入，紧时分2块 |
| `chapters/03-neuroscience.md` | 47,796 | ≈23,900 | 分块（按二级节） |
| `chapters/04-psychological-models.md` | 38,366 | ≈19,200 | 分块（按二级节） |
| `chapters/05-consciousness-suggestibility.md` | 27,503 | ≈13,800 | 可一次读入，紧时分2块 |
| `chapters/06-induction-techniques.md` | 56,723 | ≈28,400 | 分块（按二级节） |
| `chapters/07-deepening.md` | 39,505 | ≈19,800 | 分块（按二级节） |
| `chapters/08-suggestion-design.md` | 44,176 | ≈22,100 | 分块（按二级节） |
| `chapters/09-emergence-post-hypnotic.md` | 48,711 | ≈24,400 | 分块（按二级节） |
| `chapters/10-self-hypnosis.md` | 39,205 | ≈19,600 | 分块（按二级节） |
| `chapters/11-group-stage.md` | 51,602 | ≈25,800 | 分块（按二级节） |
| `chapters/12-pain-management.md` | 51,744 | ≈25,900 | 分块（按二级节） |
| `chapters/13-anxiety-trauma.md` | 47,700 | ≈23,800 | 分块（按二级节） |
| `chapters/14-psychotherapy-integration.md` | 44,270 | ≈22,100 | 分块（按二级节） |
| `chapters/15-medical-applications.md` | 50,137 | ≈25,100 | 分块（按二级节） |
| `chapters/16-pediatric-hypnosis.md` | 49,441 | ≈24,700 | 分块（按二级节） |
| `chapters/17-addiction-habits.md` | 41,331 | ≈20,700 | 分块（按二级节） |
| `chapters/18-recent-advances.md` | 46,501 | ≈23,300 | 分块（按二级节） |
| `chapters/19-neuroimaging.md` | 28,155 | ≈14,100 | 可一次读入，紧时分2块 |
| `chapters/20-ai-vr.md` | 37,290 | ≈18,600 | 分块（按二级节） |
| `chapters/21-cross-cultural.md` | 33,401 | ≈16,700 | 分块（按二级节） |
| `chapters/22-ethics-legal.md` | 43,416 | ≈21,700 | 分块（按二级节） |

### 3.3 实战模块（五件套）

| 文件 | 字节 | ≈token | 读入建议 |
|---|---:|---:|---|
| `scripts/催眠脚本库.md` | 66,643 | ≈33,300 | 分块（按脚本号切） |
| `exercises/训练练习册.md` | 56,004 | ≈28,000 | 分块（按二级节） |
| `case-studies/实战案例集.md` | 64,182 | ≈32,100 | 分块（按案例号切） |
| `case-studies/场景案例集.md` | 59,298 | ≈29,600 | 分块（按案例号切） |

### 3.4 参考与规范

| 文件 | 字节 | ≈token | 读入建议 |
|---|---:|---:|---|
| `references/core-papers.md` | 13,964 | ≈7,000 | 一次性读入 |
| `references/verification-status.md` | 15,077 | ≈7,500 | 一次性读入 |
| `references/练习题参考答案.md` | 39,248 | ≈19,600 | 分块（按二级节） |
| `references/编辑规范.md` | 6,978 | ≈3,500 | 一次性读入 |
| `references/llm-usage.md` | 26,510 | ≈13,300 | 可一次读入，紧时分2块（本文件） |

### 3.5 附录（57 个）

| 文件 | 字节 | ≈token | 读入建议 |
|---|---:|---:|---|
| `appendix/a-scales.md` | 15,692 | ≈7,800 | 一次性读入 |
| `appendix/aa-intergenerational-trauma.md` | 34,068 | ≈17,000 | 分块（按二级节） |
| `appendix/ab-creativity-innovation.md` | 28,225 | ≈14,100 | 可一次读入，紧时分2块 |
| `appendix/ac-extreme-environments.md` | 28,607 | ≈14,300 | 可一次读入，紧时分2块 |
| `appendix/ad-human-enhancement-ethics.md` | 23,813 | ≈11,900 | 可一次读入，紧时分2块 |
| `appendix/ae-cross-species.md` | 22,293 | ≈11,100 | 可一次读入，紧时分2块 |
| `appendix/af-hypnosis-psychedelics.md` | 27,120 | ≈13,600 | 可一次读入，紧时分2块 |
| `appendix/ag-practitioner-self-care.md` | 31,772 | ≈15,900 | 可一次读入，紧时分2块 |
| `appendix/ah-sleep-medicine.md` | 41,556 | ≈20,800 | 分块（按二级节） |
| `appendix/ai-aging-dementia.md` | 38,597 | ≈19,300 | 分块（按二级节） |
| `appendix/aj-pain-science.md` | 35,205 | ≈17,600 | 分块（按二级节） |
| `appendix/ak-advanced-techniques.md` | 47,040 | ≈23,500 | 分块（按二级节） |
| `appendix/al-therapeutic-relationship.md` | 28,143 | ≈14,100 | 可一次读入，紧时分2块 |
| `appendix/am-complex-cases.md` | 38,956 | ≈19,500 | 分块（按二级节） |
| `appendix/an-trauma-informed.md` | 30,755 | ≈15,400 | 可一次读入，紧时分2块 |
| `appendix/ap-quality-assurance.md` | 28,902 | ≈14,500 | 可一次读入，紧时分2块 |
| `appendix/aq-pain-translation.md` | 39,395 | ≈19,700 | 分块（按二级节） |
| `appendix/ar-trauma-neurobiology.md` | 36,882 | ≈18,400 | 分块（按二级节） |
| `appendix/as-emotion-regulation.md` | 35,883 | ≈17,900 | 分块（按二级节） |
| `appendix/at-mind-body-medicine.md` | 30,661 | ≈15,300 | 可一次读入，紧时分2块 |
| `appendix/au-cognitive-enhancement.md` | 32,588 | ≈16,300 | 分块（按二级节） |
| `appendix/av-gut-brain-axis.md` | 46,026 | ≈23,000 | 分块（按二级节） |
| `appendix/aw-microbiome-brain.md` | 36,550 | ≈18,300 | 分块（按二级节） |
| `appendix/ax-neuroimmunology.md` | 37,099 | ≈18,500 | 分块（按二级节） |
| `appendix/ay-epigenetics-clinical.md` | 36,965 | ≈18,500 | 分块（按二级节） |
| `appendix/az-neuroendocrinology.md` | 34,975 | ≈17,500 | 分块（按二级节） |
| `appendix/b-glossary.md` | 45,011 | ≈22,500 | 分块（按二级节） |
| `appendix/ba-cardioneurology.md` | 43,544 | ≈21,800 | 分块（按二级节） |
| `appendix/bb-respiratory-medicine.md` | 36,440 | ≈18,200 | 分块（按二级节） |
| `appendix/bc-rehabilitation.md` | 37,478 | ≈18,700 | 分块（按二级节） |
| `appendix/bd-psychopharmacology.md` | 39,908 | ≈20,000 | 分块（按二级节） |
| `appendix/be-telehealth-digital.md` | 32,643 | ≈16,300 | 分块（按二级节） |
| `appendix/d-certifications.md` | 15,414 | ≈7,700 | 一次性读入 |
| `appendix/e-supervision.md` | 19,388 | ≈9,700 | 可一次读入，紧时分2块 |
| `appendix/f-research-overview.md` | 13,398 | ≈6,700 | 一次性读入 |
| `appendix/g-safety-manual.md` | 18,458 | ≈9,200 | 可一次读入，紧时分2块 |
| `appendix/h-therapy-comparison.md` | 14,596 | ≈7,300 | 一次性读入 |
| `appendix/i-failure-difficulties.md` | 16,499 | ≈8,200 | 可一次读入，紧时分2块 |
| `appendix/j-cross-reference.md` | 11,938 | ≈6,000 | 一次性读入 |
| `appendix/k-chinese-context.md` | 18,346 | ≈9,200 | 可一次读入，紧时分2块 |
| `appendix/l-index.md` | 16,508 | ≈8,300 | 可一次读入，紧时分2块 |
| `appendix/m-clinical-quickref.md` | 18,287 | ≈9,100 | 可一次读入，紧时分2块 |
| `appendix/n-research-methods.md` | 17,675 | ≈8,800 | 可一次读入，紧时分2块 |
| `appendix/o-study-guide.md` | 22,109 | ≈11,100 | 可一次读入，紧时分2块 |
| `appendix/p-research-corrections.md` | 24,140 | ≈12,100 | 可一次读入，紧时分2块 |
| `appendix/practical-tools.md` | 18,889 | ≈9,400 | 可一次读入，紧时分2块 |
| `appendix/q-emerging-therapies.md` | 27,633 | ≈13,800 | 可一次读入，紧时分2块 |
| `appendix/r-health-economics.md` | 24,238 | ≈12,100 | 可一次读入，紧时分2块 |
| `appendix/s-consciousness-science.md` | 28,796 | ≈14,400 | 可一次读入，紧时分2块 |
| `appendix/t-patient-experience.md` | 32,737 | ≈16,400 | 分块（按二级节） |
| `appendix/treatment-protocols.md` | 22,009 | ≈11,000 | 可一次读入，紧时分2块 |
| `appendix/u-neuroplasticity.md` | 23,692 | ≈11,800 | 可一次读入，紧时分2块 |
| `appendix/v-historical-cases.md` | 41,887 | ≈20,900 | 分块（按二级节） |
| `appendix/w-gender-diversity.md` | 29,922 | ≈15,000 | 可一次读入，紧时分2块 |
| `appendix/x-sports-performance.md` | 26,578 | ≈13,300 | 可一次读入，紧时分2块 |
| `appendix/y-organizational.md` | 29,426 | ≈14,700 | 可一次读入，紧时分2块 |
| `appendix/z-future-trends.md` | 27,623 | ≈13,800 | 可一次读入，紧时分2块 |

---

## 四、给 LLM 流水线的建议

1. **先读头部摘要**：每个文件前 30 行有摘要块（章节是“📋 核心内容摘要”，导读与工具篇是“📌 本篇摘要”），独立成立——读完就知道这是什么、适用什么场景、关键结论、去哪里深入。命中再展开正文，不命中直接换文件。

2. **RAG 按二级节切分**：章节按 `## X.Y`、附录按 `## X.N` 或 `## 一、`、脚本库按 `## 脚本N` 切。每块不超过 4K token，块头带上“文件名+上级标题+本节标题”三级上下文，别把小节标题丢掉。

3. **单次调用控制在约 8K token**：检索块+指令+输出合计约 8K。引用原文以小节为单位取，不整文件塞；一次回答涉及多个主题时，分多次检索再合并，不要贪多。

4. **超时与重试从断点小节继续**：任务清单以小节号为粒度（如 `chapters/12 12.4`）；超时或失败只重试未完成的小节，已完成的不再重读。同一文件并发切块时，给每个任务固定的小节号区间，避免重复计费。

5. **输出引用格式**：`文件路径+小节号`，例如 `chapters/12-pain-management.md 12.7` 或 `appendix/ah-sleep-medicine.md AH.4`。不写“见上文”这类查不到的指向。

6. **安全闸门（硬约束，优先于效率）**：
   - 任何临床建议类输出必须附“不构成医疗建议”提示，并指向 [DISCLAIMER](../DISCLAIMER.md)；
   - 不得生成“恢复记忆”“年龄退行取证”类脚本与话术；
   - 高风险技术（年龄退行、快速诱导、创伤处理）输出必须带 ⚠️ 警示；
   - 案例与示例数字必须带“示意”标注；
   - 用户处于危机（自伤、自杀、急性精神症状）时，只输出危机热线与转介建议，不做治疗性对话。

7. **冲突处理**：练习题答案与正文冲突时以正文为准；术语以 [编辑规范](编辑规范.md) 为准；版本戳以 README 为准，模型不得自行改写。

---

## 五、机器可读约定

| 标记或结构 | 含义 | 机器怎么用 |
|---|---|---|
| `> **📋 核心内容摘要**` | 章节文件的头部摘要块 | 前 30 行即可判定文件是否相关 |
| `> **📌 本篇摘要**` | 导读、工具篇的头部摘要块 | 同上，格式为“这是什么/适用场景/关键结论/去哪里深入” |
| `> - **场景关键词**：A｜B｜C` | 摘要块末行的检索关键词（3-6 个，全角竖线分隔） | 直接建倒排索引，等价于路由表左列 |
| `> **🔗 前后衔接**：前置…；本篇解决…；深入…` | 读前需要什么、读完去哪里 | 拼接阅读序列，替代人工猜上下文 |
| Markdown 表格 | 并列参数、判据、对照、流程 | 优先解析表格而非长段落 |
| `> **⚠️` 开头的提示块 | 安全红线 | 生成内容时必须原样带出，不得删减 |
| `## X.Y` / `## 一、` | 二级节，最小检索单元 | 切分、断点续跑、引用定位的统一粒度 |
| “教学性改编示例”“示意” | 案例与数字为虚构教学材料 | 输出时必须保留该标注，不得当真实数据引用 |
| `*版本：…*`（文件尾） | 版本戳 | 只读，模型不得改写 |
| 章节四件套 | 摘要→正文→延伸阅读→思考题→术语表→返回目录 | 缺任一项视为文件不完整，先报错再处理 |

**术语锁定**（检索同义词归一）：规范词是催眠感受性、后催眠暗示、暗示感受性（suggestibility，与催眠感受性分开建索引）；被禁用的旧写法清单见 [编辑规范](编辑规范.md) 第 2 节（全书唯一允许保留禁用词作反例的文件），检索索引里把旧写法一律归一到规范词。

---

*本书内容不构成医疗建议，AI 输出涉及临床场景时须回挂 [DISCLAIMER](../DISCLAIMER.md) 的安全红线。*
