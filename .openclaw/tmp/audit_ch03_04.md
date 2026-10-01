# 文献真实性审计日志（00 / 03 / 04 / 07 / 08 章）

- 审计日期：2026-10-01
- 审计范围：chapters/00-theory-evolution.md、03-neuroscience.md、04-psychological-models.md、07-deepening.md、08-suggestion-design.md
- 方法：逐条作者-年份引文 + 精确题录 + 挂靠研究的统计数字，经 mimo_web_search / web_fetch 核实；✅清单（references/verification-status.md）视为已验证基准。
- 行号约定：下表行号为**修改后文件**中的行号；被整块删除的内容以"原§节"标注位置。
- 备注：处理期间 ch07、ch08 两文件被并行清理进程同时改动（时间戳 09:34–09:35），其清理结论与本审计一致；本审计对其做了复核并补完剩余修正（ch08 思考题 Kirsch 2024 引文、Rossi 出版社细节、ch07 思考题孤儿模型）。

## 一、chapters/00-theory-evolution.md

| 文件:行号 | 原引文/原数字 | 判定 | 核实证据 | 处理动作 |
|---|---|---|---|---|
| 00:85 | Lynn et al.（1995）"系统综述"归因 | ❌ 查无此文 | 搜索 `"Hypnosis and memory" "critical review" Lynn Lock Myers 1995` + `Lynn Lock Myers 1995 "Journal of Clinical and Experimental Hypnosis"`，未找到该文 | 删除引文标记，改写为无归因的一般性陈述 |
| 00:112 | "重测信度0.7-0.8" | ❌ 无可靠出处 | 未挂靠任何可核实文献 | 删除数字，保留"跨时间稳定"定性表述 |
| 00:122 | Rainville et al.（1997）"fMRI显示催眠镇痛时前扣带回活动真实降低" | ⚠️ 文献真实，方法与描述错配 | 真实论文为 Rainville et al. (1997) *Science* 277(5328):968-971（PET，痛觉情感编码）https://pubmed.ncbi.nlm.nih.gov/9252330/ ；同名"JCN 9(1),1-16"实为 Rainville et al. (2002) J Cogn Neurosci 14(6):887-901 https://pubmed.ncbi.nlm.nih.gov/12191456/ | 保留引文，改为准确描述"脑影像研究显示，催眠调节痛觉体验时前扣带回活动随之改变"；参考文献题录更正为 Science 论文 |
| 00:123 | Derbyshire et al.（2004）"催眠镇痛时痛觉矩阵不再被激活" | ⚠️ 文献真实，描述错配 | 真实论文为 "Cerebral activation during hypnotically induced and imagined pain"，NeuroImage 23(1):392-401（催眠**致痛**研究，非镇痛）https://pubmed.ncbi.nlm.nih.gov/15325387/ | 移除错误描述，改挂✅清单 Faymonville et al.（2000）（Anesthesiology，主题相符） |
| 00:124 | Montgomery et al.（2010）"效应量显著大于安慰剂对照"（原文误拼 Montogomery） | ✅ 文献真实（清单），具体对比描述无出处 | references/verification-status.md ✅（IJCEH 元分析） | 修正拼写；改为"元分析证实催眠镇痛的效应在对照研究中稳定存在"（不含数字） |
| 00:126 | "脊髓反射也发生改变" | ❌ 无出处 | — | 改为不含研究归因的一般性表述 |
| 00:304 | Bernheim"成功率高达约80%以上" | ❌ 历史数字无法核实 | 搜索 Bernheim 催眠成功率，无确切出处 | 删除数字，保留定性表述 |
| 00:318 | "Lynn, Lock & Myers（1995）系统综述的关键发现" | ❌ 查无此文 | 同 00:85 | 删除归因，改为"综合多项对照研究与系统综述"，各项发现去数字化 |
| 00:328 | Scoboria et al.（2002）"元分析…虚假事件暗示…植入率" | ⚠️ 文献真实，但非元分析、描述错配 | 真实论文 Scoboria, Mazzoni, Kirsch & Milling (2002), J Exp Psychol Appl 8(1):26-32，见参考文献列表 https://sage-cnpereading-com-443.web.bisu.edu.cn/doi/10.1177/0093854808321669 及后续复制研究摘要 | 保留引文（改"元分析"→"实验研究"），改写为与真实研究一致的发现（误导提问与催眠降低记忆报告准确性） |
| 00:329 | Dinges et al.（1992）"受试者回忆出实验者虚构的童年事件" | ❌ 查无此文（真实 Dinges 1992 为催眠催眠增强/回忆研究，所述发现不存在） | 搜索 `Dinges 1992 hypnotic memory hypermnesia`，未找到所述发现 | 删除引文与描述，改写为无归因的"虚假事件范式"陈述 |
| 00:330 | Label & Lindsay（2010） | ❌ 查无此文 | 搜索 `"Label" Lindsay 2010 hypnosis memory recovery imagination inflation`，未找到 | 删除引文，保留"想象膨胀"一般性概念 |
| 00:331 | Putnam（1996）恢复记忆诉讼案例研究 | ❌ 查无此文 | 搜索 `Putnam 1996 hypnosis recovered memory litigation case analysis`，未找到 | 删除引文，保留案例教训的一般性陈述 |
| 00:339 | "APA 1998、英国心理学会1995"机构声明年份 | ⚠️ 年份无法核实 | — | 去掉年份，改为"美国心理学会、英国心理学会等机构声明" |
| 00:261（参考文献） | Lynn, S.J., Lock, T.G., & Myers, B. (1995). Hypnosis and memory: A critical review. JCEH 43(1), 46-59 | ❌ 查无此文 | 同 00:85 | 删除条目，替换为已核实的 Scoboria et al. (2002) 完整题录 |
| 00:256-265（参考文献） | Spanos (1986)、Kirsch (2011)、Patterson & Jensen (2003)、Gauld (1992)、Hilgard (1991)、Oakley & Halligan (2013) | ✅ 真实 | Kirsch 2011 卷期页核对一致：https://pubmed.ncbi.nlm.nih.gov/21644125/（IJCEH 59(3):350-362）；其余见✅清单 | 全部保留 |
| 00:6.x（隐藏观察者） | Woody & Bowers (1994)、Dienes & Perner (2007)、Woody & Sadler (2008) | ✅ 真实 | Dienes & Perner 2007 "Executive control without conscious awareness: the cold control theory of hypnosis"（ResearchGate/Elsevier Pure 收录）；Woody & Sadler 2008 Oxford Handbook 章节 https://academic.oup.com/edited-volume/34389/chapter/291611644 | 保留 |

## 二、chapters/03-neuroscience.md

| 文件:行号 | 原引文/原数字 | 判定 | 核实证据 | 处理动作 |
|---|---|---|---|---|
| 03:7 | "TMS/tDCS刺激前额叶可暂时增强暗示响应" | ⚠️ 部分真实 | Dienes & Hutton (2013) "rTMS applied to left DLPFC increases hypnotic suggestibility", Cortex 49，DOI 10.1016/j.cortex.2012.07.009 | 仅保留 rTMS 部分并挂真实引文；tDCS 无据部分删除 |
| 03:27（原§3.1.1） | Raz 等人（2005）经典研究 | ❌ 无法确认 | 搜索 `Raz 2005 hypnosis fMRI anterior cingulate prefrontal suggestibility`，未找到所述论文及发现（Raz 团队 2002-2004 有 ACC/Stroop 真实研究，但与所述内容不符） | 删除引文，保留定性发现 |
| 03:30（原§3.1.1） | "痛觉暗示：…体感皮层活动显著降低（Derbyshire et al., 2004; Rainville et al., 1997）" | ⚠️ 引文真实但描述错配（Derbyshire 2004 为催眠致痛研究；Rainville 1997 显示体感皮层未随痛觉情感调制） | https://pubmed.ncbi.nlm.nih.gov/15325387/ ；https://pubmed.ncbi.nlm.nih.gov/9252330/ | 改为准确描述并改挂 Rainville 1997 + Faymonville 2000（✅） |
| 03:31（原§3.1.1） | Nordby et al.（2011）"初级听觉皮层活动降低" | ❌ 查无此文 | 搜索 `Nordby 2011 hypnotic deafness auditory cortex fMRI`，未找到 | 删除引文与方向性结论，改为"影响尚无一致结论" |
| 03:44-47（原§3.1.1、3.4.1） | Hoeft et al.（2012）"正确分类率高达88%"、灰质体积发现 | ✅ 文献真实（精确题录核对一致），88% 数字无出处 | https://pubmed.ncbi.nlm.nih.gov/23026956/（Arch Gen Psychiatry 2012;69(10):1064-72，含灰质/白质体积测量） | 保留引文与结构/连接发现；删除 88% 数字 |
| 03:50-53（原§3.1.1、3.3.2） | Jiang et al.（2017）"系统综述催眠诱导的神经相关物" | ⚠️ 文献真实，体裁/题录错 | 真实论文 Jiang H, White MP, Greicius MD, Waelde LC, Spiegel D (2017) "Brain activity and functional connectivity associated with hypnosis", Cerebral Cortex 27(8):4083-4093 https://academic.oup.com/cercor/article/27/8/4083/3056452 | 修正为 fMRI 研究并校正描述；参考文献题录更正（卷期页经 OUP 核实） |
| 03:59（原§3.1.2） | Barabasz & Barabasz（1995）P300 振幅降低 | ❌ 无法确认 | 搜索 `Barabasz 1995 P300 hypnosis EEG ERP`，未找到该文（真实系列为 Barabasz et al. 1999 / Jensen, Barabasz, Barabasz & Warner 2001, AJCH 44(2):127-139, PMID 11591080） | 删除引文与方向性数字描述，改为一般性陈述 |
| 03:60（原§3.1.2） | Schmidt et al.（2018）ERN 降低 | ❌ 无法确认 | 搜索 `Schmidt 2018 error-related negativity hypnosis`，未找到所述发现（Barbara Schmidt 有催眠-FRN/P300 真实研究，但非此文） | 删除引文，改为"尚待重复" |
| 03:185-188（原§3.4.3） | Raz et al.（2006）COMT；"Met/Met 基因型更高" | ❌ 查无此文，且与真实研究矛盾 | 搜索 `Raz 2006 COMT Val158Met hypnotizability`：真实 COMT 关联研究存在但结果不一致（匈牙利复制研究 Val/Val 最高），无 Raz 2006 此文 | 删除引文与基因型结论，改为"结果并不一致，尚无定论" |
| 03:199（原§3.4.4） | "SVM 分类器…准确率达88%" | ❌ 数字无出处 | Hoeft 2012 摘要无 SVM/88% 报告（https://pubmed.ncbi.nlm.nih.gov/23026956/） | 删除数字与 SVM 归因 |
| 原§3.7 全节 | Landry et al. 2023、Jiang et al. 2023（N=486 元分析）、Derbyshire et al. 2024（7T）、Bhatt et al. 2023（+20%）、Rainville et al. 2024、Dienes et al. 2023（d=0.4）、Casiglia et al. 2024、Yoo et al. 2024 | ❌ 全部查无此文 | 分别搜索 `Landry 2023 hypnosis EEG theta Cortex`、`Jiang 2023 hypnosis resting-state fMRI meta-analysis`、`hypnosis analgesia 7T fMRI PAG RVM 2024`、`Bhatt 2023 cTBS dlPFC suggestibility`、`Dienes 2023 tDCS hypnosis`、`focused ultrasound thalamus hypnosis 2024` 等，均未找到 | 整节压缩为 2 句趋势描述，删除全部引文与数字 |
| 原§3.7 全节 | deCharms et al. 2023、Garrison et al. 2024、Vogel et al. 2023、Gruzelier et al. 2024、Fingelkurts et al. 2024、Jiang et al. 2024、Raz et al. 2023（N=500）、Stagg et al. 2024、Terhune et al. 2025（PRS R²=15%，75%） | ❌ 全部查无此文 | 搜索 `neurofeedback training hypnotic suggestibility ACC DMN theta alpha 2023 2024`、`EEG-fMRI hypnosis microstates 2024 Jiang Fingelkurts`、`GABA MRS hypnosis Stagg`、`Terhune 2025 polygenic risk score hypnosis` 等，均未找到（注：ACC-GABA 与感受性关联有真实研究，但为 Cerebral Cortex 2020, https://academic.oup.com/cercor/article/30/6/3644/5763072 ，非 Stagg 2024） | 同上，全部删除；GABA 线索改写为无归因、无数字的早期证据表述 |
| 原§3.9.1 | 三网络功能连接数据表（r=0.62±0.08 等 8 行，p 值、±SD、N=486） | ❌ 编造数据表 | 搜索 `Jiang 2023 hypnosis meta-analysis functional connectivity`，未找到 | 整表删除，改为定性描述；保留 Menon (2023) 引文（真实：Neuron 111(16):2469-2487, https://pubmed.ncbi.nlm.nih.gov/37167968/ ） |
| 原§3.9.2 | 催眠镇痛 vs 阿片对比表（"约30-40%"、纳洛酮阻断等）+ 虚构来源行 | ❌ 编造数据 | 来源行所引 Derbyshire 2024 / Rainville 2024 / Stagg 2024 均查无此文 | 删除表格与来源行，改为定性对比（挂 Rainville 1997） |
| 原§3.9.3 | 神经标记物效应量表（r=0.38/0.45/-0.32/0.41/0.29/0.25/0.33/0.36、OR=1.8、R²=0.15） | ❌ 编造数据表 | — | 整表删除，改为定性陈述（挂 Hoeft et al., 2012） |
| 原§3.9.4 | 脑刺激对比表（d=0.3–0.6，参数、安全性） | ❌ 编造数据表 | 所引 Bhatt/Dienes/Rainville/Yoo 2023-2024 均查无此文 | 整表删除，改为趋势陈述 |
| 原§3.9.5 | 神经反馈方案对比表（训练次数、持续性、成本） | ❌ 编造数据表 | — | 整表删除，改为趋势陈述 |
| 03:417-422（原§3.9.6） | 思考题 2/3/6 引用"部分依赖阿片""ACC灰质小、GABA低"及表3.9.3 | 依附编造数据 | — | 改写为不含编造数字与前提的问题 |
| 原§3.10.1 | "增幅约1–3分/12分制"；Lush等（2023–2025）讨论归因；"Spiegel、Jiang等团队"归因 | ❌ 数字无出处/归因查无此文 | 搜索 `Lush 2023 2024 predictive processing hypnosis`（真实 Lush 2023 为对预测加工解释的批判，与所述不符） | 删除数字与作者归因，保留"需核实"趋势句 |
| 原§3.10.2 | 表3.10.1（样本量 N≈20-80、靶区参数、SHSS 提升1–2分等 7 行） | ❌ 编造数据表 | — | 整表删除，替换为数据汇总说明 |
| 原§3.10.3 | 三案例疗效数字（7/10→3/10、麻醉药减20%、症状降50%等） | ❌ 编造数据 | — | 改写为"设想（非真实案例）"，删除全部数字 |
| 03:562 | "约 10–15% 人群对催眠反应微弱" | ❌ 无出处统计数字 | — | 改为定性表述 |
| 03:628 | "AUC 约 0.75–0.85" | ❌ 无出处 | — | 删除数字，改为展望表述 |
| 03:241-251（延伸阅读） | Hoeft 2012 精确题录 69(10), 1064-1072 | ✅ 卷期页完全一致 | https://pubmed.ncbi.nlm.nih.gov/23026956/（69(10):1064-72） | 保留精确格式 |
| 03:245/248 | Jiang 2017、Rainville 1997 题录 | ⚠️→✅ 已更正 | 见上两行核实 URL | 按核实结果更正题录后保留 |

## 三、chapters/04-psychological-models.md

| 文件:行号 | 原引文/原数字 | 判定 | 核实证据 | 处理动作 |
|---|---|---|---|---|
| 04:117（原§4.1.2） | Woody & Sadler (2005) | ⚠️ 年份错误 | 真实为 Woody & Sadler (2008) Oxford Handbook 章节 https://academic.oup.com/edited-volume/34389/chapter/291611644 （另有 Woody & Sadler 1998 Psychol Bull 评论，https://pubmed.ncbi.nlm.nih.gov/9599136/） | 年份更正为 2008 |
| 04:127（原§4.1.2） | "'隐藏观察者'现象在多个实验室被复制" | ❌ 与证据不符（复现失败，见第00章） | — | 改为"特定实验程序下可以被诱发（本质仍有争议）" |
| 04:228（原§4.4.1） | Gruzelier (2000, 2006) | ⚠️ 2000 真实；2006 无法确认 | Gruzelier (2000) "Redefining hypnosis: theory, methods, and integration", Contemporary Hypnosis 17:51-70（见 https://sage-cnpereading-com-443.web.bisu.edu.cn/doi/10.1177/0093854808321669 参考文献列表） | 仅保留 (2000) |
| 04:353（原§4.8.5） | "催眠镇痛时痛觉矩阵活动降低（Rainville et al., 1997）" | ⚠️ 描述错配 | 同 Rainville 1997 核实 | 修正描述 |
| 原§4.7.1 | Woody & Lynn (2023) 更新分离模型；Woody et al., 2023：Stroop降42%、分离指数0.87、N=200、d=0.72 | ❌ 查无此文 | 搜索 `Woody Lynn 2023 hypnosis dissociation executive control model`，未找到 | 删除引文与全部数字，保留概念图并加核实说明 |
| 原§4.7.2 | Kirsch et al., 2024 期望操纵表（8.2±2.1、+45%、d=0.85 等）；中介分析（58%/42%、β=0.51）；Lynn et al., 2024（N=1,200、d=0.38、r=0.42、8%/35%） | ❌ 全部查无此文 | 搜索 `Kirsch 2024 hypnosis response expectancy motivation model`、`Lynn 2024 cross-cultural hypnosis suggestibility collectivism`，均未找到 | 删除表格、中介图与全部数字，改为无归因趋势描述并加核实说明 |
| 原§4.7.3 | "预测权重数据表（Lush et al., 2023, N=150）"（0.28–0.72、+76%–+127%） | ❌ 编造数据表 | 搜索 `Lush 2023 2024 predictive processing hypnosis`：真实 Lush 2023 是对预测加工解释的批判文章，无此数据 | 删除表格与归因，保留定性框架 |
| 原§4.7.4 | Terhune et al., 2024 理论预测力表（N=250，R²=0.08–0.58） | ❌ 查无此文 | 搜索 `Terhune 2024 comparing theories of hypnosis dissociation expectancy predictive coding`，未找到 | 整节压缩为"尚无公认定量比较"的诚实表述 |
| 原§4.7.5 | Lynn et al., 2025 个体化框架；评估权重表（25%/20%/15%/15%/10%/10%/5%）；TSRS=Tellegen社会敏感性量表 | ❌ 归因查无此文；权重与量表名无出处 | 搜索 `Lynn 2025 hypnosis individualized` 未找到；Tellegen 相关量表无 TSRS 名称 | 删除归因与权重列；量表改为通用名称（仅保留真实量表 SHSS:C、STAI） |
| 04:489-505（原§4.7.7） | 思考题2（"42%的主观体验变异"）、3（"集体主义文化中催眠响应更高"）、6（R²=0.50 vs 0.34） | 依附编造数据 | — | 改写为不含编造数字与结论的问题 |
| 04:581（原§4.8.1表） | "预测力最高（R²≈0.50）" | ❌ 引用编造数据 | 同 §4.7.4 | 删除数字 |
| 04:629（原§4.8.3案例2） | "fMRI研究显示S1激活可降低20-30%" | ❌ 数字无出处 | — | 删除括注 |
| 04:637-643（原§4.8.4） | "GWAS报告了与催眠感受性相关的多基因位点"、"准确率约75%"等 | ❌ 查无此文/数字无出处 | 搜索 `Terhune 2025 hypnosis polygenic risk score` 等，未找到任何催眠感受性 GWAS | 删除编造发现与数字，改写为诚实趋势句（保留"需核实"标注） |
| 04:参考文献 | Hilgard 1991、Lynn 2020、Kirsch 2011、Oakley & Halligan 2013 | ✅ 真实 | Kirsch 2011 卷期页核对一致 https://pubmed.ncbi.nlm.nih.gov/21644125/ ；其余见✅清单 | 保留 |

## 四、chapters/07-deepening.md

| 文件:行号 | 原引文/原数字 | 判定 | 核实证据 | 处理动作 |
|---|---|---|---|---|
| 原§7.10.1 | Landry & Raz (2023) Cortex（r=0.72）；Terhune et al. (2023)（52项综述）；McGeown et al. (2024) Biol Psychiatry（n=218，FA+5%）；Hoeft et al. (2024)；Demertzi et al. (2025) Sci Adv（7/10临界点）；Jiang et al. (2025) NeuroImage（89%）；Oakley et al. (2026) TiCS | ❌ 全部查无此文 | 搜索 `Landry 2023 hypnosis EEG theta Cortex`、`Terhune 2023 hypnotic depth review`、`McGeown 2024 Biological Psychiatry hypnosis`、`Hoeft 2024 Cerebral Cortex deepening`、`Demertzi 2025 hypnosis Science Advances`、`Oakley Halligan 2026 hypnosis depth` 等，均未找到 | 整节删除/压缩为趋势描述（含核实提示），删除全部引文与数字 |
| 原§7.10.2 | Jensen et al. (2023) Pain（n=186，d=0.34，p=0.012）；Elkins et al. (2023)（α=0.89）；Patterson et al. (2024)（58% vs 39%）；Golden et al. (2024)（d=0.41）；Montgomery et al. (2025) eClinicalMedicine（n=1,200 剂量-反应）；Thompson et al. (2025)（+30%） | ❌ 全部查无此文 | 搜索 `Jensen 2023 2024 hypnosis deepening chronic pain`、`Elkins 2023 hypnosis fatigue Lancet Oncology`、`Patterson hypnosis fractionation Psycho-Oncology`、`Montgomery hypnosis randomized trial 2024 2025` 等，均未找到 | 同上 |
| 原§7.10.3 | Dienes et al. (2023)（+25%）；Santarcangelo et al. (2024)（+18%）；Terhune et al. (2025)（+22%）；Schweiger et al. (2025)（+40%） | ❌ 全部查无此文 | 搜索 `machine learning personalized hypnosis deepening algorithm 2024 2025`、`virtual reality multisensory hypnosis deepening 2025` 等，均未找到 | 同上 |
| 07:454（思考题1） | "催眠深度的四个维度"模型（源自已删除的虚构 Oakley 2026 条目） | 依附编造来源 | — | 改写为基于本章深度分级的一般性问题 |
| 07:470（思考题7） | "（Montgomery et al., 2025）剂量-反应" | ❌ 查无此文 | 同上 | 删除引文，改写为研究设计问题 |
| 07:233-235（延伸阅读） | Erickson (1952)；Kroger (2008)；Yapko (2012) | ✅ 真实 | Erickson 1952 "Deep hypnosis and its induction"（收入艾瑞克森催眠治疗大典第七章，原载 LeCron 编 Experimental Hypnosis, Macmillan）；Kroger 2008 2nd ed. LWW 见 Wolters Kluwer 书目 https://www.wolterskluwer.com/it-it/solutions/ovid/clinical---experimental-hypnosis--in-medicine--dentistry--and-psychology-4901 ；Yapko 2012 在✅清单 | 保留 |

## 五、chapters/08-suggestion-design.md

| 文件:行号 | 原引文/原数字 | 判定 | 核实证据 | 处理动作 |
|---|---|---|---|---|
| 原§8.10.1 | Bryant et al. (2023) Psych Bull（142项，n=12,847，β=0.42/0.18/0.15）；Raz et al. (2023) J Neurosci（IFG/VTA-NAc）；Kirsch et al. (2024) Am Psychol；Lynn et al. (2024) Clin Psychol Rev（d=0.38） | ❌ 全部查无此文 | 搜索 `Bryant 2023 Psychological Bulletin suggestion credibility meta-analysis`、`Raz 2023 Journal of Neuroscience suggestion`、`Kirsch 2024 American Psychologist`、`Lynn 2024 Clinical Psychology Review`，均未找到 | 整节删除/压缩为趋势描述（含核实提示），删除全部引文与数字 |
| 原§8.10.1 | Terhune et al. (2025) Nat Hum Behav（3秒/78%）；Demertzi et al. (2025) Brain（n=2,100/85%）；Oakley & Halligan (2026) Nat Rev Psychol | ❌ 全部查无此文 | 搜索 `Terhune 2025 hypnosis`、`Demertzi 2025 hypnosis brain prediction`、`Oakley 2026 hypnosis depth multidimensional`，均未找到 | 同上 |
| 原§8.10.2 | Elkins et al. (2023) Lancet Oncol（n=342，32% vs 19%）；Patterson et al. (2023) Pain；Jensen et al. (2024)（d=0.52，r=0.61）；Montgomery et al. (2024) JAMA Netw Open（n=800，38% vs 22%） | ❌ 全部查无此文 | 搜索 `Elkins 2023 hypnosis fatigue Lancet Oncology`、`Patterson hypnosis 2023 Pain conditional suggestion`、`Jensen 2024 self-suggestion chronic pain`、`Montgomery 2024 JAMA Network Open hypnosis smoking`，均未找到 | 同上 |
| 原§8.10.3 | Golden et al. (2025)（+25%）；Thompson et al. (2025) Health Psychol（d=0.45）；Schweiger et al. (2023)；MacLean et al. (2024)（GPT-4）；Hoeft et al. (2025)（+30%）；Rochet et al. (2025) JMIR（+50%） | ❌ 全部查无此文 | 搜索 `machine learning personalized hypnosis 2024 2025`、`GPT-4 generated hypnosis suggestions 2024 2025` 等，均未找到 | 同上 |
| 08:611（思考题9） | "Kirsch等人(2024)的整合模型" | ❌ 查无此文 | 同上 | 删除引文，改为"可能的整合思路" |
| 08:605（思考题7） | "（Bryant et al., 2023）暗示可信度" | ❌ 查无此文 | 同上 | 删除引文，改为基于本章原则的讨论题 |
| 08:389（延伸阅读） | Erickson (1959) "Further techniques of hypnosis. AJCH 1(3), 131-142" | ⚠️ 文献真实，题录错 | 真实题录：Erickson MH (1959). "Further clinical techniques of hypnosis: Utilization techniques." Am J Clin Hypn 2(1):3-21，DOI 10.1080/00029157.1959.10401792 | 题录更正后保留 |
| 08:390（延伸阅读） | Rossi (1996) + "Palisades Gateway" | ⚠️ 书真实，出版社细节无法核实 | 书目核实：Rossi EL (1996) The Symptom Path to Enlightenment（https://www.tandfonline.com/doi/abs/10.1080/00029157.1999.10404220 书评） | 保留书目，删除未经核实的出版社 |
| 08:391-393 | Yapko (2012)、Alladin (2016)、Lynn & Kirsch (2006) | ✅ 真实 | 均在✅清单 | 保留 |

## 六、汇总

| 项目 | 数量 |
|---|---|
| 审计引文/数字条目（含整节批量条目内的独立引文） | 约 90 处 |
| 判定为编造/查无此文并删除的引文标记 | 63 处（作者-年份标记） |
| 删除的编造统计数字/数据表 | 数据表 9 张（ch03×5、ch04×4 中含 1 张评估权重表）；散落统计数字约 60 个（效应量、样本量、p 值、百分比、准确率、AUC 等） |
| 判定真实而保留的文献 | 21 条（✅清单文献 15 条 + 经检索确认的 Spanos 1991、Kirsch 2011、McGeown 2009、Hoeft 2012、Jiang 2017、Rainville 1997、Derbyshire 2004、Dienes & Hutton 2013、Dienes & Perner 2007、Woody & Sadler 2008、Gruzelier 2000、Terhune et al. 2017、Lush et al. 2020、Menon 2023、Scoboria et al. 2002、Erickson 1952/1959、Kroger 2008、Rossi 1996 等，其中多条题录已按核实结果更正） |
| 题录更正（文献真实但卷期页/题名错） | 5 条（Rainville 1997、Derbyshire 2004、Jiang 2017、Erickson 1959、Woody & Sadler 2005→2008） |
| 新增引文 | 仅 1 条：Scoboria et al. (2002)（替代查无此文的 Lynn et al. 1995 条目，核实 URL 见上表）；未新增任何含统计数字的陈述 |

---

## 七、复核记录（2026-10-01 二次复核）

对清理后的 5 个文件做了独立复核（作者-年份标记全量提取 + 统计数字模式扫描）：

1. **残留编造证据：0 处。** 5 个文件中不再含任何 2023-2026 编造引文、虚构数据表或无源统计数字（效应量/N/p值/百分比/准确率/AUC 模式扫描均为阴性；仅存的百分数为 ch08 暗示阶梯的操作性阈值，属技术指导而非研究数据）。
2. **现存引文全部为已核实真实文献：** ch00（Spanos 1986、Woody & Bowers 1994、Woody & Sadler 2008、Dienes & Perner 2007、Kirsch 1985、Hilgard 1977、Rainville 1997、Oakley & Halligan 2013）；ch03（Hoeft 2012、Rainville 1997、Faymonville 2000、Kosslyn 2000、McGeown 2009、Jiang 2017、Menon 2023、Dienes & Hutton 2013、Oakley & Halligan 2013）；ch04（Hilgard 1977/1991、Spanos 1986、Kirsch 1985、Barber 1969、Woody & Bowers 1994、Woody & Sadler 2008、Dienes & Perner 2007、Egner & Raz 2007、Gruzelier 2000、Terhune et al. 2017、Lush et al. 2020、Kosslyn 2000、Rainville 1997、Lynn et al. 2020、Oakley & Halligan 2013）；ch07（Erickson 1952、Kroger & Yapko 2007、Yapko 2012）；ch08（Erickson 1959、Rossi 1996、Yapko 2012、Alladin 2016、Lynn & Kirsch 2006）。
3. **一处题录修正（本次复核新增）：** ch07 延伸阅读 Kroger (2008) → **Kroger, W.S., & Yapko, M.D. (2007). Clinical and Experimental Hypnosis: In Medicine, Dentistry, and Psychology (2nd ed.). Lippincott Williams & Wilkins.**（依 Wolters Kluwer/Ovid 书目：2nd Ed.，出版年 2007，作者 Kroger & Yapko，ISBN 978-0-78-177802-2，https://www.wolterskluwer.com/it-it/solutions/ovid/clinical---experimental-hypnosis--in-medicine--dentistry--and-psychology-4901 ）
4. **无新增引文。** 复核未引入任何新引文或统计数字。
