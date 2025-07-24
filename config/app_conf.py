SYSTEM_PROMPT = """You are an expert on frontend design, you will always respond to web design tasks.
Your task is to create a website according to the user's request using either native HTML or React framework
When choosing implementation framework, you should follow these rules:

[Implementation Rules]
1. You should use React by default.
2. When the user requires HTML, choose HTML to implement the request.
3. If the user requires a library that is not installed in current react environment, please use HTML and tell the user the reason.
4. After choosing the implementation framework, please follow the corresponding instruction.

[HTML Instruction]
You are a powerful code editing assistant capable of writing code and creating artifacts in conversations with users, or modifying and updating existing artifacts as requested by users. 
All code is written in a single code block to form a complete code file for display, without separating HTML and JavaScript code. An artifact refers to a runnable complete code snippet, you prefer to integrate and output such complete runnable code rather than breaking it down into several code blocks. For certain types of code, they can render graphical interfaces in a UI window. After generation, please check the code execution again to ensure there are no errors in the output.
Do not use localStorage as it is not supported by current environment.
Output only the HTML, without any additional descriptive text.

[React Instruction]
You are an expert on frontend design, you will always respond to web design tasks.
Your task is to create a website using a SINGLE static React JSX file, which exports a default component. This code will go directly into the App.jsx file and will be used to render the website.

## Common Design Principles

Regardless of the technology used, follow these principles for all designs:

### General Design Guidelines:
- Create a stunning, contemporary, and highly functional website based on the user's request
- Implement a cohesive design language throughout the entire website/application
- Choose a carefully selected, harmonious color palette that enhances the overall aesthetic
- Create a clear visual hierarchy with proper typography to improve readability
- Incorporate subtle animations and transitions to add polish and improve user experience
- Ensure proper spacing and alignment using appropriate layout techniques
- Implement responsive design principles to ensure the website looks great on all device sizes
- Use modern UI patterns like cards, gradients, and subtle shadows to add depth and visual interest
- Incorporate whitespace effectively to create a clean, uncluttered design
- For images, use placeholder images from services like https://placehold.co/     
- The primary language of the generated website should be Chinese

## React Design Guidelines

### Implementation Requirements:
- Ensure the React app is a single page application
- DO NOT include any external libraries, frameworks, or dependencies outside of what is already installed
- Utilize TailwindCSS for styling, focusing on creating a visually appealing and responsive layout
- Avoid using arbitrary values (e.g., `h-[600px]`). Stick to Tailwind's predefined classes for consistency
- Use mock data instead of making HTTP requests or API calls to external services
- Utilize Tailwind's typography classes to create a clear visual hierarchy and improve readability
- Ensure proper spacing and alignment using Tailwind's margin, padding, and flexbox/grid classes
- Do not use localStorage as it is not supported by current environment.

### Installed Libraries:
You can use these installed libraries if required. 
- **lucide-react**: Lightweight SVG icon library with 1000+ icons. Import as `import { IconName } from "lucide-react"`. Perfect for buttons, navigation, status indicators, and decorative elements.
- **recharts**: Declarative charting library built on D3. Import components like `import { LineChart, BarChart } from "recharts"`. Use for data visualization, analytics dashboards, and statistical displays.
- **framer-motion**: Production-ready motion library for React. Import as `import { motion } from "framer-motion"`. Use for animations, page transitions, hover effects, and interactive micro-interactions.
- **p5.js** : JavaScript library for creative coding and generative art. Usage: import p5 from "p5". Create interactive visuals, animations, sound-driven experiences, and artistic simulations.
- **three, @react-three/fiber, @react-three/drei**: 3D graphics library with React renderer and helpers. Import as `import { Canvas } from "@react-three/fiber"` and `import { OrbitControls } from "@react-three/drei"`. Use for 3D scenes, visualizations, and immersive experiences.

You can ONLY use libraries in [lucide-react, recharts, framer-motion, p5.js, three], do NOT use uninstalled libraries!

Remember to only return code for the App.jsx file and nothing else. The resulting application should be visually impressive, highly functional, and something users would be proud to showcase.
"""


# SYSTEM_PROMPT = """你是一名前端设计专家，专门负责响应网页设计任务。
# 你的任务是根据用户需求，使用原生HTML或React框架创建网站。
# 选择实现框架时，应遵循以下规则：

# [实现规则]
# 1. 默认情况下应使用React。
# 2. 当用户要求使用HTML时，选择HTML来实现需求。
# 3. 如果用户需要的库在当前React环境中未安装，请使用HTML并告知用户原因。
# 4. 选择实现框架后，请遵循相应的指导说明。

# [HTML指导说明]
# 你是一个强大的代码编辑助手，能够在与用户的对话中编写代码和创建作品，或根据用户要求修改和更新现有作品。
# 所有代码都应放在单个代码块中，形成一个完整的代码文件进行展示，不要将HTML和JavaScript代码分开。作品指的是可运行的完整代码片段，你应优先整合并输出此类完整可运行代码，而非拆分为多个代码块。对于某些类型的代码，它们可以在UI窗口中渲染图形界面。生成后，请再次检查代码执行情况，确保输出没有错误。
# 不要使用localStorage，因为当前环境不支持。
# 只输出HTML，不包含任何额外的描述性文本。

# [React指导说明]
# 你是一名前端设计专家，专门负责响应网页设计任务。
# 你的任务是使用单个静态React JSX文件创建网站，该文件导出一个默认组件。此代码将直接放入App.jsx文件中，用于渲染网站。

# ## 通用设计原则

# 无论使用何种技术，所有设计都应遵循以下原则：

# ### 通用设计指南：
# - 根据用户需求创建一个出色、现代且功能强大的网站
# - 在整个网站/应用程序中实现连贯的设计语言
# - 选择精心挑选的、和谐的色彩搭配，提升整体美感
# - 通过适当的排版创建清晰的视觉层次结构，提高可读性
# - 融入微妙的动画和过渡效果，增添精致感并改善用户体验
# - 使用适当的布局技术确保适当的间距和对齐
# - 实施响应式设计原则，确保网站在所有设备尺寸上都美观
# - 使用现代UI模式，如卡片、渐变和微妙阴影，增添深度和视觉趣味
# - 有效利用空白，创造干净、整洁的设计
# - 对于图片，使用来自 https://placehold.co/ 等服务的占位图片
# - 生成的网站主要语言应为中文

# ## React设计指南

# ### 实现要求：
# - 确保React应用是单页应用
# - 不要包含任何当前已安装之外的外部库、框架或依赖项
# - 利用TailwindCSS进行样式设计，专注于创建视觉吸引力强且响应式的布局
# - 避免使用任意值（例如`h-[600px]`）。坚持使用Tailwind的预定义类以保持一致性
# - 使用模拟数据，而不是对外部服务进行HTTP请求或API调用
# - 利用Tailwind的排版类创建清晰的视觉层次结构并提高可读性
# - 使用Tailwind的边距、内边距和flexbox/grid类确保适当的间距和对齐
# - 不要使用localStorage，因为当前环境不支持。

# ### 已安装的库：
# 如果需要，你可以使用这些已安装的库。
# - **lucide-react**：轻量级SVG图标库，包含1000多个图标。导入方式为`import { IconName } from "lucide-react"`。非常适合按钮、导航、状态指示器和装饰元素。
# - **recharts**：基于D3构建的声明式图表库。导入组件的方式如`import { LineChart, BarChart } from "recharts"`。用于数据可视化、分析仪表板和统计显示。
# - **framer-motion**：适用于React的生产级动画库。导入方式为`import { motion } from "framer-motion"`。用于动画、页面过渡、悬停效果和交互式微交互。
# - **p5.js**：用于创意编程和生成艺术的JavaScript库。使用方法：import p5 from "p5"。创建交互式视觉效果、动画、声音驱动的体验和艺术模拟。
# - **three、@react-three/fiber、@react-three/drei**：3D图形库，带有React渲染器和辅助工具。导入方式为`import { Canvas } from "@react-three/fiber"`和`import { OrbitControls } from "@react-three/drei"`。用于3D场景、可视化和沉浸式体验。

# 记住只返回App.jsx文件的代码，不要返回其他内容。生成的应用程序应该具有令人印象深刻的视觉效果、强大的功能，是用户会自豪地展示的作品。
# """

SERVICE_NAME = "Qwen-Coder"

# DEMO_LIST = [
#     {
#         "card": {"index": 0},
#         "title": "高校课程管理系统",
#         "description": "一个贴合管理系统风格的高校课程管理前端界面。",
#         "prompt": "设计一个 **高校管理系统**，贴合管理系统风格的高校课程管理前端界面，核心需求围绕多角色业务流程与管理系统典型交互展开：\n"
#                    "1. 核心业务流程：\n"
#                    "   - 多角色登录与功能区：支持学生、教师、管理员角色登录，登录后通过**左侧侧边栏**切换功能模块（如个人中心、课程管理、成绩管理、系统设置等），侧边栏需体现层级菜单，可折叠/展开；\n"
#                    "   - 个人中心数据看板：登录后默认进入个人中心，以**卡片化布局**展示用户基础信息（姓名、角色、学院/部门），关联数据以快捷入口呈现（学生：已选课程数、待评课程数；教师：已授课程数、待录入成绩数 ）；\n"
#                    "   - 课程管理列表操作：\n"
#                      "     - 学生端：「可选课程列表」以**表格形式**呈现（含课程名称、学分、教师、上课时间、剩余容量），支持批量选课、搜索筛选（按课程名/教师/学院），选课后实时同步至个人中心「已选课程」；\n"
#                      "     - 教师端：「课程管理」表格展示已授课程（含课程名称、选课人数、最近课件发布时间），支持**行内操作**（编辑课程信息、发布课件、录入/修改成绩），点击「录入成绩」跳转至成绩管理页；\n"
#                      "     - 管理员端：「课程总览」表格覆盖全校课程，支持批量导入/导出课程数据、调整课程权限（开放选课/关闭选课）；\n"
#                    "   - 成绩管理流程：教师通过课程列表进入成绩页，以**弹窗/抽屉**形式录入成绩，支持按学生姓名/学号搜索，录入后学生端个人中心「成绩查询」模块实时更新，支持学生导出成绩单（PDF/Excel）；\n"
#                    "2. 页面关联与交互：\n"
#                    "   - 全局交互：顶部保留搜索栏（支持跨模块搜索，如课程名、学生姓名），右上角可快速切换角色（管理员需切换身份模拟操作时）、退出登录；\n"
#                    "   - 列表操作联动：课程列表点击课程名称，以**新标签页/弹窗**打开课程详情（含课程介绍、教学大纲、课件资源）；成绩页操作记录可追溯（如谁在何时修改过成绩）；\n"
#                    "   - 侧边栏与内容区联动：切换侧边栏菜单时，右侧内容区平滑切换对应页面，保留面包屑导航（如「课程管理 > 已授课程 > 大学英语」），支持快速返回上级；\n"
#                    "   - 数据反馈与加载：涉及数据提交（如选课、改成绩）时，以**加载态/成功提示**反馈操作结果，异常情况（如选课冲突、成绩格式错误）弹出明确报错，引导用户修正。",

#     },
#     {
#         "card": {"index": 1},
#         "title": "医院患者信息管理系统",
#         "description": "一个贴合管理系统风格的医院患者信息管理前端界面。",
#         "prompt": "设计一个 **医院患者信息管理系统**， 贴合医院管理场景的患者信息管理前端界面，核心需求围绕医疗业务流程与管理系统交互逻辑展开：\n"
#                     "1. 核心业务流程：\n"
#                     "   - 多角色登录与功能区：支持医生、护士、管理员、医护人员等角色登录，登录后通过**左侧侧边栏**切换功能模块（如患者档案、住院管理、诊疗记录、系统设置等 ），侧边栏采用可折叠层级菜单，适配不同使用场景；\n"
#                     "   - 患者档案数据看板：登录后默认进入患者档案概览，以**卡片化 + 表格结合**布局，展示今日新入院患者数、待复诊患者数、危急患者数等关键数据，支持快速搜索患者（按姓名、病历号、住院号 ）；\n"
#                     "   - 患者信息管理操作：\n"
#                         "     - 医生端：「患者档案列表」以**表格形式**呈现（含患者姓名、年龄、性别、入院时间、诊断结果、当前科室、床位号 ），支持**行内操作**（查看完整病历、录入诊疗记录、开具检查/处方、标记病情等级 ），点击「诊疗记录」跳转至详情页；\n"
#                         "     - 护士端：「住院管理列表」展示在院患者（含患者姓名、护理等级、体温、血压、下次护理时间 ），支持批量记录生命体征、调整护理计划、标记出院待办，操作后同步更新患者档案；\n"
#                         "     - 管理员端：「全院患者总览」表格覆盖全科室患者，支持批量导入/导出患者基础信息、设置数据权限（如医生可查看的患者范围 ）、维护科室与床位关联关系；\n"
#                     "   - 诊疗流程管理：医生通过患者列表进入诊疗记录页，以**弹窗/抽屉**形式录入医嘱、检查结果、手术信息，支持按时间轴查看历史诊疗轨迹，护士执行医嘱后（如输液、采血 ），系统自动标记执行状态并同步给医生；\n"
#                     "2. 页面关联与交互：\n"
#                     "   - 全局交互：顶部保留快捷搜索栏（支持跨模块搜索患者、诊疗项目 ），右上角可快速切换角色（管理员模拟医护操作校验 ）、查看系统通知（如危急值预警、待处理医嘱 ）；\n"
#                     "   - 列表操作联动：患者档案列表点击患者姓名，以**新标签页/弹窗**打开完整病历（含既往病史、过敏史、历次检查报告、手术记录 ），诊疗记录操作留痕（如谁在何时录入/修改过医嘱 ）；\n"
#                     "   - 侧边栏与内容区联动：切换侧边栏菜单时，右侧内容区平滑切换对应页面，保留面包屑导航（如「患者管理 > 住院患者 > 302 病房 XX 患者」 ），支持快速返回上级菜单；\n"
#                     "   - 数据反馈与预警：涉及关键操作（如危急值录入、患者病情突变标记 ）时，以**醒目弹窗 + 声音提醒**反馈，异常情况（如病历号重复、检查结果格式错误 ）弹出明确报错并引导修正，保障医疗数据准确。",
#     },
#     {
#         "card": {"index": 2},
#         "title": "一站式综合在线商城平台",
#         "description": "一个涵盖全品类商品销售与服务的在线商城前端界面。",
#         "prompt": "设计一个 **一站式综合在线商城平台**，贴合电商零售场景的全流程购物体验，核心需求围绕商品交易链路与多角色操作逻辑展开：\n"
#                     "1. 核心业务流程：\n"
#                     "   - 多角色登录与功能区：支持普通用户、商家、管理员三类角色登录，登录后通过**顶部导航栏 + 左侧功能区**区分操作模块（用户端：商品浏览、订单管理、个人中心；商家端：商品管理、订单处理、数据分析；管理员端：平台运营、用户管理、权限配置），角色切换保留操作痕迹；\n"
#                     "   - 商品展示与发现：首页采用**瀑布流 + 模块化**布局，顶部轮播展示促销活动，下方按品类划分专区（生鲜、服饰、数码等），每个专区包含「热销榜」「新品推荐」「限时折扣」子模块，支持通过**标签筛选**（价格区间、好评率、配送方式）快速定位商品；\n"
#                     "   - 商品交易全流程：\n"
#                         "     - 用户端：商品详情页包含「图文展示」「规格选择」「评价晒单」「相似推荐」标签页，支持「加入购物车」「立即购买」双路径，结算页采用**分步引导**（确认商品 > 选择地址 > 支付方式 > 订单确认），支付后跳转实时订单跟踪页；\n"
#                         "     - 商家端：「订单管理中心」以**状态分组表格**呈现（待付款、待发货、已发货、售后中），支持批量打印物流单、修改发货状态、发起主动营销（如补差价链接），商品管理页提供「批量上架/下架」「库存预警设置」「SKU组合管理」功能；\n"
#                         "     - 管理员端：「平台数据看板」展示日活、转化率、客单价等核心指标，支持按区域、时段、品类生成数据报表，「违规处理」模块可对商品、店铺执行下架、处罚操作，维护平台规范；\n"
#                     "   - 会员体系与营销：用户端集成「会员等级」「积分商城」「优惠券中心」，支持积分抵现、优惠券叠加使用，商家端可创建「满减活动」「限时秒杀」「拼团玩法」，活动页面自动生成分享链接；\n"
#                     "2. 页面关联与交互：\n"
#                     "   - 全局交互：顶部固定「搜索栏」支持跨品类搜索，输入时实时显示「热门搜索」「历史记录」，右侧悬浮「购物车图标」实时更新商品数量，点击弹出迷你购物车；\n"
#                     "   - 商品操作联动：商品列表页支持「长按批量选择」「左滑快速加购」，详情页规格选择后实时更新价格与库存，评价区支持「图/文筛选」「有用度排序」，点击评价图片可放大查看；\n"
#                     "   - 订单状态流转：下单后通过「进度时间轴」展示订单状态（支付 > 商家接单 > 仓库发货 > 物流运输 > 确认收货），物流信息实时同步并推送短信通知，售后申请以「表单 + 图片上传」形式提交，处理进度可追踪；\n"
#                     "   - 个性化体验：基于用户浏览历史，在「猜你喜欢」模块推荐相似商品，支持「足迹清除」「兴趣标签编辑」，首次访问用户通过「偏好选择」弹窗快速定位感兴趣品类，提升浏览效率。"
#     },
# ]



# DEMO_LIST = [
#     {
#         "card": {"index": 0},
#         "title": "系统登录页",
#         "description": "高校课程管理系统的静态登录界面，含角色选择展示",
#         "prompt": "设计「高校课程管理系统」的静态登录页面（仅展示UI，无需交互逻辑）：\n"
#                    "1. 页面结构：\n"
#                    "   - 左侧品牌区：显示系统名称「高校课程管理系统」、校训标语（如「立德树人 格物致知」）、简约校园插画（教学楼/图书馆线条图）；\n"
#                    "   - 右侧登录区：白色卡片式布局，包含：\n"
#                      "     - 输入框占位展示：「用户名（学号/工号）」「密码」（显示默认提示文字，无需输入功能）；\n"
#                      "     - 静态按钮：「登录」（蓝色主按钮，仅展示样式）、「忘记密码」（灰色文字链接）；\n"
#                      "     - 角色选择区：登录按钮下方显示「学生」「教师」「管理员」三个静态标签（默认选中「学生」，用底色区分）；\n"
#                    "2. 样式要求：\n"
#                    "   - 配色：主色#165DFF（蓝色），辅助色#E8F3FF（浅蓝背景），文字#333333（正文）、#666666（辅助文字）；\n"
#                    "   - 布局：左右分栏（左侧占40%，右侧占60%），整体居中显示，适配1280px及以上屏幕；\n"
#                    "   - 细节：输入框带圆角（4px），按钮hover样式（仅静态展示，无需实际效果），底部显示「© 2024 某某大学教务处」。"
#     },
#     {
#         "card": {"index": 1},
#         "title": "个人中心页面",
#         "description": "高校课程管理系统的用户个人信息静态展示页面",
#         "prompt": "设计「高校课程管理系统」的个人中心静态页面（仅展示UI，无需交互）：\n"
#                    "1. 页面结构：\n"
#                    "   - 顶部信息栏：显示系统名称+「个人中心」面包屑（首页 > 个人中心）；\n"
#                    "   - 用户信息卡：左侧头像（灰色占位图+姓名「张三」），右侧展示基础信息（角色：学生；学院：计算机学院；学号：2022001001；入学年份：2022）；\n"
#                    "   - 数据概览区：3个横向卡片，分别显示：\n"
#                      "     - 已选课程：「5门」（下方小字「总学分：15」）；\n"
#                      "     - 待完成事项：「2项」（下方小字「含1门课程评价」）；\n"
#                      "     - 平均成绩：「85分」（下方小字「专业排名：前15%」）；\n"
#                    "   - 近期课程表：表格展示未来3天课程（日期、课程名称、时间、地点），无操作按钮；\n"
#                    "2. 样式要求：\n"
#                    "   - 卡片风格：白色背景+轻微阴影，信息卡顶部用主色#165DFF作为标题栏；\n"
#                    "   - 布局：顶部信息栏+用户信息卡（占1/3高度）+下方两栏（左：数据卡片；右：课程表）；\n"
#                    "   - 静态提示：所有数据为示例展示，无点击/编辑功能。"
#     },
#     {
#         "card": {"index": 2},
#         "title": "课程列表页面",
#         "description": "高校课程管理系统的课程列表静态展示页面",
#         "prompt": "设计「高校课程管理系统」的课程列表静态页面（仅展示UI，无需操作逻辑）：\n"
#                    "1. 页面结构：\n"
#                    "   - 顶部：标题「课程列表」+ 筛选区（搜索框占位文字「搜索课程/教师」，学院筛选下拉框显示「全部学院」，无实际筛选功能）；\n"
#                    "   - 课程表格：表头含「课程名称」「学分」「教师」「上课时间」「上课地点」「状态」，表格内填充5条示例数据：\n"
#                      "     - 数据1：计算机网络 / 3学分 / 李老师 / 周一3-4节 / 教201 / 「已选」（绿色标签）；\n"
#                      "     - 数据2：高等数学 / 4学分 / 王老师 / 周三1-2节 / 教105 / 「可选」（蓝色标签）；\n"
#                      "     - 数据3：人工智能 / 3学分 / 张老师 / 周五5-6节 / 实302 / 「已满」（灰色标签）；\n"
#                    "   - 底部：分页器（显示「第1页 / 共3页」，左右箭头为静态样式）；\n"
#                    "2. 样式要求：\n"
#                    "   - 表格样式：隔行变色（白色/浅灰），表头底色为#F5F7FA，边框为1px浅灰；\n"
#                    "   - 状态标签：已选（绿底白字）、可选（蓝底白字）、已满（灰底白字）；\n"
#                    "   - 无操作按钮：表格无「选课」等按钮，仅展示列表数据。"
#     },
#     {
#         "card": {"index": 3},
#         "title": "课程详情页面",
#         "description": "高校课程管理系统的单门课程详情静态展示页面",
#         "prompt": "设计「高校课程管理系统」的课程详情静态页面（仅展示UI，无需交互）：\n"
#                    "1. 页面结构：\n"
#                    "   - 顶部：面包屑（首页 > 课程列表 > 计算机网络）+ 课程标题「计算机网络 - 3学分」；\n"
#                    "   - 基础信息区：左侧课程封面（灰色占位图），右侧信息列表（教师：李老师；学院：计算机学院；开课学期：2024秋；考核方式：考试）；\n"
#                    "   - 内容标签页：3个标签「课程介绍」「教学大纲」「课件列表」，默认显示「课程介绍」：\n"
#                      "     - 课程介绍：文本「本课程介绍计算机网络基本原理、TCP/IP协议及应用...」；\n"
#                      "     - 课件列表（静态展示）：2条示例（第1周：网络基础.pdf；第2周：TCP协议.ppt）；\n"
#                    "2. 样式要求：\n"
#                    "   - 标签页：当前标签（课程介绍）底部显示蓝色下划线，其他标签为灰色文字；\n"
#                    "   - 布局：基础信息区占1/3高度，标签页内容占2/3高度，整体宽度与系统其他页面一致；\n"
#                    "   - 静态元素：所有文本、标签为展示用，无点击跳转功能。"
#     },
#     {
#         "card": {"index": 4},
#         "title": "成绩查询页面",
#         "description": "高校课程管理系统的学生成绩静态展示页面",
#         "prompt": "设计「高校课程管理系统」的成绩查询静态页面（仅展示UI，无需操作）：\n"
#                    "1. 页面结构：\n"
#                    "   - 顶部：标题「成绩查询」+ 学期筛选（显示「2024年秋季学期」，无实际筛选功能）；\n"
#                    "   - 成绩概览：1个主卡片显示「学期平均成绩：85.5」，下方2个小卡片：「已通过课程：5门」「未完成课程：0门」；\n"
#                    "   - 成绩表格：表头含「课程名称」「学分」「平时成绩」「期末成绩」「总评成绩」，填充3条数据：\n"
#                      "     - 数据1：计算机网络 / 3 / 80 / 88 / 85（黑色文字）；\n"
#                      "     - 数据2：高等数学 / 4 / 90 / 82 / 85（黑色文字）；\n"
#                    "   - 底部：「导出成绩单」按钮（灰色静态样式，无点击功能）；\n"
#                    "2. 样式要求：\n"
#                    "   - 成绩突出：总评成绩用稍大字体，平均成绩卡片用主色#165DFF作为背景；\n"
#                    "   - 布局：顶部标题+成绩概览（1行3卡）+ 成绩表格（占2/3高度）；\n"
#                    "   - 无编辑功能：所有分数为静态展示，无输入框/修改按钮。"
#     },
#     {
#         "card": {"index": 5},
#         "title": "系统首页页面",
#         "description": "高校课程管理系统的首页静态展示页面",
#         "prompt": "设计「高校课程管理系统」的首页静态页面（仅展示UI，无需交互）：\n"
#                    "1. 页面结构：\n"
#                    "   - 顶部导航栏：左侧系统名称「高校课程管理系统」，右侧显示「张三 同学」+ 头像占位图；\n"
#                    "   - 功能入口区：4个横向大卡片，分别对应系统核心功能：\n"
#                      "     - 课程管理：图标（书本）+ 文字「课程管理」；\n"
#                      "     - 成绩查询：图标（成绩单）+ 文字「成绩查询」；\n"
#                      "     - 个人中心：图标（用户）+ 文字「个人中心」；\n"
#                      "     - 通知公告：图标（铃铛）+ 文字「通知公告」；\n"
#                    "   - 通知公告区：标题「最新通知」，下方3条静态通知（带日期）：\n"
#                      "     - 「2024-09-01 关于秋季学期选课时间调整的通知」；\n"
#                      "     - 「2024-08-25 2022级学生成绩复核申请通知」；\n"
#                    "   - 底部：版权信息「© 2024 某某大学教务处 版权所有」；\n"
#                    "2. 样式要求：\n"
#                    "   - 导航栏：浅灰背景，固定顶部；\n"
#                    "   - 功能卡片：白色背景+阴影，图标用主色#165DFF，hover样式仅静态展示（无实际效果）；\n"
#                    "   - 布局：顶部导航栏+功能入口区（占1/2高度）+ 通知公告区（占1/2高度）。"
#     }
# ]

WEB_TEMPLATE = """
import React from 'react';
import { Home, User, Folder, Settings, LogOut } from 'lucide-react';
import { motion } from 'framer-motion';
import dayjs from 'dayjs';

const App = () => {
  // 系统信息配置
  const systemConfig = {
    name: 'XXXX管理系统',   //根据对应系统变化
    adminName: 'admin',
    currentTime: dayjs().format('YYYY-MM-DD HH:mm')
  };

  return (
    <div className="min-h-screen flex bg-slate-50">
      {/* 左侧侧边栏*/}
      <motion.aside 
        className="bg-slate-800 text-slate-100 w-64 flex flex-col items-center justify-start p-4 shadow-md" 
        initial={{ x: -50 }} 
        animate={{ x: 0 }} 
        transition={{ duration: 0.3 }}
      >
        {/* 顶部系统名称 */}
        <div className="w-full py-4 mb-8 border-b border-slate-700">
          <h1 className="text-xl font-bold text-center tracking-wide text-white">
            {systemConfig.name}
          </h1>
        </div>
        
        {/* 导航菜单*/}
        <nav className="w-full flex-grow">
          <ul className="space-y-1">
            <li>
              <a href="#" className="flex items-center px-4 py-3 text-sm font-medium rounded-lg bg-indigo-600 text-white">
                <Home className="mr-3 h-5 w-5" />
                功能1
              </a>
            </li>
            <li>
              <a href="#" className="flex items-center px-4 py-3 text-sm font-medium text-slate-200 hover:bg-slate-700 hover:text-white rounded-lg transition-colors duration-200">
                <User className="mr-3 h-5 w-5" />
                功能2
              </a>
            </li>
            <li>
              <a href="#" className="flex items-center px-4 py-3 text-sm font-medium text-slate-200 hover:bg-slate-700 hover:text-white rounded-lg transition-colors duration-200">
                <Folder className="mr-3 h-5 w-5" />
                功能3
              </a>
            </li>
            <li>
              <a href="#" className="flex items-center px-4 py-3 text-sm font-medium text-slate-200 hover:bg-slate-700 hover:text-white rounded-lg transition-colors duration-200">
                <Settings className="mr-3 h-5 w-5" />
                功能4
              </a>
            </li>
          </ul>
        </nav>
        
        {/* 底部退出按钮 */}
        <div className="w-full pt-4 border-t border-slate-700 mt-4">
          <button className="flex items-center justify-center w-full px-4 py-2 text-sm font-medium text-slate-200 hover:bg-slate-700 hover:text-white rounded-lg transition-colors duration-200">
            <LogOut className="mr-2 h-4 w-4" />
            退出登录
          </button>
        </div>
      </motion.aside>


      {/* 右侧主内容区*/}
      <div className="flex-1 flex flex-col">
        {/* 顶部导航栏*/}
        <header className="bg-white border-b border-slate-200 px-6 py-3 flex items-center justify-between shadow-sm">
          <div className="text-lg font-semibold text-slate-800">
            首页
          </div>
          <div className="flex items-center space-x-6">
            <span className="text-slate-600 text-sm">
              管理员：{systemConfig.adminName}
            </span>
            <span className="text-slate-500 text-sm">
              {systemConfig.currentTime}
            </span>
          </div>
        </header>

        {/* 页面主体内容 */}
        <main className="flex-1 p-6 overflow-auto">
          <div className="bg-white rounded-lg shadow-sm border border-slate-100 p-6">
            <h2 className="text-xl font-bold mb-4 text-slate-800">欢迎使用</h2>
            <p className="text-slate-600">
              这里是{systemConfig.name}的主页面，您可以通过左侧菜单导航到不同功能模块。
            </p>
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
"""

DEMO_LIST = [
    {
        "card": {"index": 0},
        "title": "个人中心",
        "description": "宠物医院管理系统个人信息与快捷数据展示页",
        "prompt": "设计「宠物医院管理系统」的「个人中心」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「个人中心」菜单项（位于功能栏顶部，图标为用户头像轮廓）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：系统名称「宠物医院管理系统」，面包屑「首页 / 个人中心」；\n"
                 "   - 主体：\n"
                 "     - 用户信息卡：左侧头像占位（圆形灰色背景），右侧显示姓名「王医生」、角色「医生」、科室「犬科」、工号「D2023001」；\n"
                 "     - 数据概览：3个横向卡片，分别展示「今日接诊 8 只（已完成 5 只）」「待处理事项 3 项（含 2 个预约确认）」「客户满意度 98%（近 30 天评价）」；\n"
                 "     - 近期日程：表格展示未来 3 天安排（日期、时间段、事项、宠物名称）；\n"
                 "3. 样式要求：\n"
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 1},
        "title": "用户管理",
        "description": "宠物医院客户信息与会员数据管理页",
        "prompt": "设计「宠物医院管理系统」的「用户管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「用户管理」菜单项（图标为用户列表轮廓，位于功能栏第二项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「客户管理」，搜索框（占位文字「搜索客户姓名/电话」），会员等级筛选下拉（默认「全部等级」）；\n"
                 "   - 主体：\n"
                 "     - 用户表格：表头含「客户ID」「姓名」「电话」「会员等级」「累计消费」「注册时间」；\n"
                 "     - 示例数据：5 条静态记录（如 C001 / 张三 / 138****5678 / 黄金会员 / ¥3200 / 2022-03-15 ）；\n"
                 "     - 底部：分页器（显示「第 1 页 / 共 5 页」，左右箭头静态）；\n"
                 "3. 样式要求：\n"
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 2},
        "title": "宠物信息管理",
        "description": "宠物档案与基础信息展示页",
        "prompt": "设计「宠物医院管理系统」的「宠物信息管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「宠物信息管理」菜单项（图标为宠物轮廓，位于功能栏第三项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「宠物档案管理」，搜索框（占位文字「搜索宠物名称/主人姓名」）；\n"
                 "   - 主体：\n"
                 "     - 宠物卡片网格：每行 3 张卡片，包含宠物照片占位（灰色轮廓+文字）、名称「旺财」、类型「金毛」、年龄「2 岁」、主人「张三」；\n"
                 "     - 底部统计：文本「共 128 条宠物档案」；\n"
                 "3. 样式要求：\n"
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 3},
        "title": "领养管理",
        "description": "待领养宠物信息与状态展示页",
        "prompt": "设计「宠物医院管理系统」的「领养管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「领养管理」菜单项（图标为领养标识，位于功能栏第四项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「待领养宠物」，筛选区（按类型：全部/猫/狗/其他；按状态：可领养/审核中）；\n"
                 "   - 主体：\n"
                 "     - 领养卡片列表：左图（宠物照片占位）右文布局，显示名称「花花」、类型「橘猫」、年龄「1 岁」、状态「可领养（绿色标签）」；\n"
                 "     - 底部须知：文本「领养须知：需提供身份证复印件及居住证明」；\n"
                 "3. 样式要求：\n"
                 "   - 右侧卡片间间距 16px，状态标签颜色区分（可领养：绿；待审核：黄）。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 4},
        "title": "医生信息管理",
        "description": "医生团队与职称信息展示页",
        "prompt": "设计「宠物医院管理系统」的「医生信息管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「医生信息管理」菜单项（图标为医生工牌轮廓，位于功能栏第五项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「医生团队」，科室筛选（全部/犬科/猫科/异宠科）；\n"
                 "   - 主体：\n"
                 "     - 医生卡片列表：每行 2-3 张卡片，包含头像占位、姓名「李医生」、职称「主治医师」、科室「犬科」、专长「骨科手术」；\n"
                 "     - 统计信息：文本「共 12 名医生，其中主任医师 3 名，主治医师 5 名」；\n"
                 "3. 样式要求：\n"
                 "   - 右侧卡片圆形头像，职称用浅色背景标签（如主任医师：深蓝色标签）。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 5},
        "title": "挂号预约管理",
        "description": "预约挂号数据与状态管理页",
        "prompt": "设计「宠物医院管理系统」的「挂号预约管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「挂号预约管理」菜单项（图标为日历+加号，位于功能栏第六项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「预约挂号管理」，日期选择（默认「2024-07-25」）；\n"
                 "   - 主体：\n"
                 "     - 预约表格：表头含「预约号」「宠物名称」「类型」「主人」「电话」「医生」「时间段」「状态」；\n"
                 "     - 示例数据：7 条静态记录（如 Y001 / 旺财 / 金毛 / 张三 / 138****5678 / 李医生 / 09:00-10:00 / 已确认（绿色） ）；\n"
                 "     - 右侧统计：数字卡片展示「今日预约总数 15」「已确认 12」「已取消 3」；\n"
                 "3. 样式要求：\n"
                 "   - 右侧表格占 70% 宽度，统计区占 30%，状态标签颜色区分（已确认：绿；待确认：黄）。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 6},
        "title": "寄养管理",
        "description": "宠物寄养信息与状态展示页",
        "prompt": "设计「宠物医院管理系统」的「寄养管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「寄养管理」菜单项（图标为宠物屋轮廓，位于功能栏第七项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「寄养管理」，搜索框（占位文字「搜索宠物名称/主人」）；\n"
                 "   - 主体：\n"
                 "     - 寄养表格：表头含「寄养ID」「宠物名称」「类型」「主人」「入托时间」「预计出托」「状态」；\n"
                 "     - 示例数据：5 条静态记录（如 F001 / 贝贝 / 泰迪 / 王五 / 2024-07-20 / 2024-07-28 / 寄养中（蓝色） ）；\n"
                 "     - 底部：分页器（显示「第 1 页 / 共 2 页」）；\n"
                 "3. 样式要求：\n"
                 "   - 右侧表格状态标识（寄养中：蓝；已结束：灰；即将到期：橙），寄养天数自动计算展示。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 7},
        "title": "寄养结果管理",
        "description": "宠物寄养结果与评价展示页",
        "prompt": "设计「宠物医院管理系统」的「寄养结果管理」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「寄养结果管理」菜单项（图标为评价星级轮廓，位于功能栏第八项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「寄养结果记录」，时间筛选（默认「2024年7月」）；\n"
                 "   - 主体：\n"
                 "     - 结果表格：表头含「寄养ID」「宠物名称」「入托-出托」「天数」「体重变化」「健康状况」「主人评价」；\n"
                 "     - 示例数据：3 条静态记录（如 F001 / 贝贝 / 07-20至07-28 / 8天 / +0.2kg / 良好 / 服务很专业 ）；\n"
                 "     - 统计卡片：展示「平均满意度 4.8 星」「本月寄养总数 23 只」；\n"
                 "3. 样式要求：\n"
                 "   - 右侧表格体重变化用符号区分（增加：绿色↑；减少：红色↓），评价文字截断展示。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    },
    {
        "card": {"index": 8},
        "title": "宠物论坛",
        "description": "宠物养护交流与知识分享页",
        "prompt": "设计「宠物医院管理系统」的「宠物论坛」静态页面 （仅展示UI，无需交互），需包含：\n"
                 "1. 左侧功能栏：\n"
                 "   - 共包含 「个人中心」、「用户管理」、「宠物信息管理」、「领养管理」、「医生信息管理」、「挂号预约管理」、「寄养管理」、「寄养结果管理」、「宠物论坛」 共九个功能；\n"
                 "   - 当前选中：「宠物论坛」菜单项（图标为对话气泡轮廓，位于功能栏第九项）；\n"
                 "2. 右侧内容区：\n"
                 "   - 顶部：标题「宠物健康论坛」，板块导航（全部/喂养知识/疾病预防/训练技巧）；\n"
                 "   - 主体：\n"
                 "     - 帖子列表：展示标题、作者、发布时间、浏览量、回复数（如「夏季如何预防狗狗中暑？」/ 王医生 / 2024-07-20 / 328 浏览 / 25 回复 ）；\n"
                 "     - 右侧热门：显示热门话题标签（#幼犬疫苗接种时间 #老年犬护理 ）；\n"
                 "3. 样式要求：\n"
                 "   - 右侧左侧帖子区占 70%，右侧热门区占 30%，热门帖标题加粗并带「热门」标签。\n "
                 "   - 参考代码布局严格一致，你需要根据代码中对应位置进行修改\n "
                 f"   - 设计模板参考代码：{WEB_TEMPLATE}"
    }
]


REACT_IMPORTS = {
    # Qwen 2.5
    # "antd": "https://esm.sh/antd@5.21.6",
    "antd": "https://esm.sh/antd@3.26.20",
    "@ant-design/colors": "https://esm.sh/@ant-design/colors@5.0.0",
    "@ant-design/icons": "https://esm.sh/@ant-design/icons@5.3.7",
    "styled-components": "https://esm.sh/styled-components@6.1.19",
    "semantic-ui-react": "https://esm.sh/semantic-ui-react@2.1.5",
    "semantic-ui-css": "https://esm.sh/semantic-ui-css@2.5.0",
    
    # Qwen 3
    "lucide-react": "https://esm.sh/lucide-react@0.525.0",
    "recharts": "https://esm.sh/recharts@3.1.0",
    "framer-motion": "https://esm.sh/framer-motion@12.23.6",
    "matter-js": "https://esm.sh/matter-js@0.20.0",
    "p5": "https://esm.sh/p5@2.0.3",
    "konva": "https://esm.sh/konva@9.3.22",
    "react-konva": "https://esm.sh/react-konva@19.0.7",
    "three": "https://esm.sh/three@0.178.0",
    "@react-three/fiber": "https://esm.sh/@react-three/fiber@9.2.0",
    "@react-three/drei": "https://esm.sh/@react-three/drei@10.5.2",
    "@tailwindcss/browser": "https://esm.sh/@tailwindcss/browser@4.1.11",
    "react": "https://esm.sh/react@19.1.0",
    "react/": "https://esm.sh/react@19.1.0/",
    "react-dom": "https://esm.sh/react-dom@19.1.0",
    "react-dom/": "https://esm.sh/react-dom@19.1.0/",
    
    # other
    "dayjs" : "https://esm.sh/dayjs"
}