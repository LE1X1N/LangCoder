
# SystemPrompt = """You are an expert React, JavaScript, and Ant-Design Components developer with a keen eye for modern, aesthetically pleasing design.
# Your task is to create a stunning, contemporary, and highly functional website based on the user's request using a SINGLE static React JSX file, which exports a default component. 
# This code will go directly into the App.jsx file and will be used to render the website.

# General guidelines:
# - Ensure the React app is a single page application with a cohesive design language throughout.
# - DO NOT include any external libraries, frameworks, or dependencies outside of what is already installed.
# - For icons, create simple, elegant SVG icons. DO NOT use any icon libraries.
# - Use styled-components to add any style, DO NOT return any extra css file.
# - Use mock data instead of making HTTP requests or API calls to external services.
# - Implement a carefully chosen, harmonious color palette that enhances the overall aesthetic.
# - Incorporate subtle animations and transitions to add polish and improve user experience.
# - Ensure proper spacing and alignment using margin, padding, and flexbox/grid classes.
# - Implement responsive design principles to ensure the website looks great on all device sizes.
# - Use antd components like cards, form, list to add depth and visual interest.
# - Incorporate whitespace effectively to create a clean, uncluttered design.

# Focus on creating a visually striking and user-friendly interface that aligns with current web design trends. Pay special attention to:
# - Typography: Use a combination of font weights and sizes to create visual interest and hierarchy.
# - Color: Implement a cohesive color scheme that complements the content and enhances usability.
# - Layout: Design an intuitive and balanced layout that guides the user's eye and facilitates easy navigation.
# - Microinteractions: Add subtle hover effects, transitions, and animations to enhance user engagement.
# - Consistency: Maintain a consistent design language throughout all components and sections.
# Remember to only return code for the App.jsx file and nothing else. Prioritize creating an exceptional layout, styling, and reactivity. The resulting application should be visually impressive and something users would be proud to showcase.
# Remember not add any description, just return the code only.
# """

# SystemPrompt = """
# 你是一名Web开发工程师，需根据以下指令编写网页。
# 你是强大的代码编辑助手，能够通过与用户对话编写代码，创建美观、现代且功能完善的网站成果物，也能根据用户需求修改和更新现有成果物。
# 所有代码需放在单个代码块中，形成完整可展示的代码文件，不得拆分HTML和JavaScript代码。成果物指可运行的完整代码片段，你应优先整合并输出此类完整可运行代码，而非拆分为多个代码块。对于特定类型的代码，需能在UI窗口中渲染图形界面。生成后请再次检查代码执行情况，确保输出无错误。

# 通用指南：
# - 确保HTML为单页应用，整体设计风格统一。
# - 不得引入已安装依赖之外的外部库、框架或依赖。
# - 图标需使用简洁优雅的SVG格式创建矢量图，不得使用任何图标库。
# - 使用styled-components添加样式，不得返回额外的CSS文件。
# - 使用模拟数据，不得向外部服务发起HTTP请求或API调用。
# - 采用精心选择的和谐配色方案，提升整体美感。
# - 加入细微动画和过渡效果，增强精致感与用户体验。
# - 使用margin、padding及flexbox/grid布局确保间距与对齐合理。
# - 遵循响应式设计原则，确保网站在所有设备尺寸下显示正常。
# - 使用antd组件（如卡片、表单、列表）增加视觉层次感与趣味性。
# - 合理运用留白，打造简洁清爽的设计风格。

# 重点打造视觉吸引力强、用户友好的界面，符合当前Web设计趋势。特别注意：
# - 排版：结合字体粗细与大小，营造视觉层次与趣味性。
# - 色彩：采用统一配色方案，与内容互补并提升可用性。
# - 布局：设计直观平衡的布局，引导用户视线并便于导航。
# - 数据：表单/列表类组件需包含至少5条模拟数据，数据格式需贴合业务场景。
# - 微交互：添加细微的悬停效果、过渡动画，增强用户参与感。
# - 一致性：所有组件和区块保持统一的设计语言。

# 输出内容仅限HTML代码，不得包含额外描述文本。优先保证布局、样式和交互效果出色，最终应用需视觉精美且具备展示价值。
# 注意：需添加清晰注释，关键逻辑（如数据处理、表单提交）需单独封装；若涉及多角色，需通过界面元素区分操作权限；优先使用项目已导入的组件库确保兼容性。
# """


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

    

DEMO_LIST = [
    {
        "card": {"index": 0},
        "title": "高校课程管理系统",
        "description": "一个贴合管理系统风格的高校课程管理前端界面。",
        "prompt": "设计一个 **高校管理系统**，贴合管理系统风格的高校课程管理前端界面，核心需求围绕多角色业务流程与管理系统典型交互展开：\n"
                   "1. 核心业务流程：\n"
                   "   - 多角色登录与功能区：支持学生、教师、管理员角色登录，登录后通过**左侧侧边栏**切换功能模块（如个人中心、课程管理、成绩管理、系统设置等），侧边栏需体现层级菜单，可折叠/展开；\n"
                   "   - 个人中心数据看板：登录后默认进入个人中心，以**卡片化布局**展示用户基础信息（姓名、角色、学院/部门），关联数据以快捷入口呈现（学生：已选课程数、待评课程数；教师：已授课程数、待录入成绩数 ）；\n"
                   "   - 课程管理列表操作：\n"
                     "     - 学生端：「可选课程列表」以**表格形式**呈现（含课程名称、学分、教师、上课时间、剩余容量），支持批量选课、搜索筛选（按课程名/教师/学院），选课后实时同步至个人中心「已选课程」；\n"
                     "     - 教师端：「课程管理」表格展示已授课程（含课程名称、选课人数、最近课件发布时间），支持**行内操作**（编辑课程信息、发布课件、录入/修改成绩），点击「录入成绩」跳转至成绩管理页；\n"
                     "     - 管理员端：「课程总览」表格覆盖全校课程，支持批量导入/导出课程数据、调整课程权限（开放选课/关闭选课）；\n"
                   "   - 成绩管理流程：教师通过课程列表进入成绩页，以**弹窗/抽屉**形式录入成绩，支持按学生姓名/学号搜索，录入后学生端个人中心「成绩查询」模块实时更新，支持学生导出成绩单（PDF/Excel）；\n"
                   "2. 页面关联与交互：\n"
                   "   - 全局交互：顶部保留搜索栏（支持跨模块搜索，如课程名、学生姓名），右上角可快速切换角色（管理员需切换身份模拟操作时）、退出登录；\n"
                   "   - 列表操作联动：课程列表点击课程名称，以**新标签页/弹窗**打开课程详情（含课程介绍、教学大纲、课件资源）；成绩页操作记录可追溯（如谁在何时修改过成绩）；\n"
                   "   - 侧边栏与内容区联动：切换侧边栏菜单时，右侧内容区平滑切换对应页面，保留面包屑导航（如「课程管理 > 已授课程 > 大学英语」），支持快速返回上级；\n"
                   "   - 数据反馈与加载：涉及数据提交（如选课、改成绩）时，以**加载态/成功提示**反馈操作结果，异常情况（如选课冲突、成绩格式错误）弹出明确报错，引导用户修正。",

    },
    {
        "card": {"index": 1},
        "title": "医院患者信息管理系统",
        "description": "一个贴合管理系统风格的医院患者信息管理前端界面。",
        "prompt": "设计一个 **医院患者信息管理系统**， 贴合医院管理场景的患者信息管理前端界面，核心需求围绕医疗业务流程与管理系统交互逻辑展开：\n"
                    "1. 核心业务流程：\n"
                    "   - 多角色登录与功能区：支持医生、护士、管理员、医护人员等角色登录，登录后通过**左侧侧边栏**切换功能模块（如患者档案、住院管理、诊疗记录、系统设置等 ），侧边栏采用可折叠层级菜单，适配不同使用场景；\n"
                    "   - 患者档案数据看板：登录后默认进入患者档案概览，以**卡片化 + 表格结合**布局，展示今日新入院患者数、待复诊患者数、危急患者数等关键数据，支持快速搜索患者（按姓名、病历号、住院号 ）；\n"
                    "   - 患者信息管理操作：\n"
                        "     - 医生端：「患者档案列表」以**表格形式**呈现（含患者姓名、年龄、性别、入院时间、诊断结果、当前科室、床位号 ），支持**行内操作**（查看完整病历、录入诊疗记录、开具检查/处方、标记病情等级 ），点击「诊疗记录」跳转至详情页；\n"
                        "     - 护士端：「住院管理列表」展示在院患者（含患者姓名、护理等级、体温、血压、下次护理时间 ），支持批量记录生命体征、调整护理计划、标记出院待办，操作后同步更新患者档案；\n"
                        "     - 管理员端：「全院患者总览」表格覆盖全科室患者，支持批量导入/导出患者基础信息、设置数据权限（如医生可查看的患者范围 ）、维护科室与床位关联关系；\n"
                    "   - 诊疗流程管理：医生通过患者列表进入诊疗记录页，以**弹窗/抽屉**形式录入医嘱、检查结果、手术信息，支持按时间轴查看历史诊疗轨迹，护士执行医嘱后（如输液、采血 ），系统自动标记执行状态并同步给医生；\n"
                    "2. 页面关联与交互：\n"
                    "   - 全局交互：顶部保留快捷搜索栏（支持跨模块搜索患者、诊疗项目 ），右上角可快速切换角色（管理员模拟医护操作校验 ）、查看系统通知（如危急值预警、待处理医嘱 ）；\n"
                    "   - 列表操作联动：患者档案列表点击患者姓名，以**新标签页/弹窗**打开完整病历（含既往病史、过敏史、历次检查报告、手术记录 ），诊疗记录操作留痕（如谁在何时录入/修改过医嘱 ）；\n"
                    "   - 侧边栏与内容区联动：切换侧边栏菜单时，右侧内容区平滑切换对应页面，保留面包屑导航（如「患者管理 > 住院患者 > 302 病房 XX 患者」 ），支持快速返回上级菜单；\n"
                    "   - 数据反馈与预警：涉及关键操作（如危急值录入、患者病情突变标记 ）时，以**醒目弹窗 + 声音提醒**反馈，异常情况（如病历号重复、检查结果格式错误 ）弹出明确报错并引导修正，保障医疗数据准确。",
    },
    {
        "card": {"index": 2},
        "title": "一站式综合在线商城平台",
        "description": "一个涵盖全品类商品销售与服务的在线商城前端界面。",
        "prompt": "设计一个 **一站式综合在线商城平台**，贴合电商零售场景的全流程购物体验，核心需求围绕商品交易链路与多角色操作逻辑展开：\n"
                    "1. 核心业务流程：\n"
                    "   - 多角色登录与功能区：支持普通用户、商家、管理员三类角色登录，登录后通过**顶部导航栏 + 左侧功能区**区分操作模块（用户端：商品浏览、订单管理、个人中心；商家端：商品管理、订单处理、数据分析；管理员端：平台运营、用户管理、权限配置），角色切换保留操作痕迹；\n"
                    "   - 商品展示与发现：首页采用**瀑布流 + 模块化**布局，顶部轮播展示促销活动，下方按品类划分专区（生鲜、服饰、数码等），每个专区包含「热销榜」「新品推荐」「限时折扣」子模块，支持通过**标签筛选**（价格区间、好评率、配送方式）快速定位商品；\n"
                    "   - 商品交易全流程：\n"
                        "     - 用户端：商品详情页包含「图文展示」「规格选择」「评价晒单」「相似推荐」标签页，支持「加入购物车」「立即购买」双路径，结算页采用**分步引导**（确认商品 > 选择地址 > 支付方式 > 订单确认），支付后跳转实时订单跟踪页；\n"
                        "     - 商家端：「订单管理中心」以**状态分组表格**呈现（待付款、待发货、已发货、售后中），支持批量打印物流单、修改发货状态、发起主动营销（如补差价链接），商品管理页提供「批量上架/下架」「库存预警设置」「SKU组合管理」功能；\n"
                        "     - 管理员端：「平台数据看板」展示日活、转化率、客单价等核心指标，支持按区域、时段、品类生成数据报表，「违规处理」模块可对商品、店铺执行下架、处罚操作，维护平台规范；\n"
                    "   - 会员体系与营销：用户端集成「会员等级」「积分商城」「优惠券中心」，支持积分抵现、优惠券叠加使用，商家端可创建「满减活动」「限时秒杀」「拼团玩法」，活动页面自动生成分享链接；\n"
                    "2. 页面关联与交互：\n"
                    "   - 全局交互：顶部固定「搜索栏」支持跨品类搜索，输入时实时显示「热门搜索」「历史记录」，右侧悬浮「购物车图标」实时更新商品数量，点击弹出迷你购物车；\n"
                    "   - 商品操作联动：商品列表页支持「长按批量选择」「左滑快速加购」，详情页规格选择后实时更新价格与库存，评价区支持「图/文筛选」「有用度排序」，点击评价图片可放大查看；\n"
                    "   - 订单状态流转：下单后通过「进度时间轴」展示订单状态（支付 > 商家接单 > 仓库发货 > 物流运输 > 确认收货），物流信息实时同步并推送短信通知，售后申请以「表单 + 图片上传」形式提交，处理进度可追踪；\n"
                    "   - 个性化体验：基于用户浏览历史，在「猜你喜欢」模块推荐相似商品，支持「足迹清除」「兴趣标签编辑」，首次访问用户通过「偏好选择」弹窗快速定位感兴趣品类，提升浏览效率。"
    },
    {
        "card": {"index": 3},
        "title": "经典贪吃蛇游戏",
        "description": "一款还原经典玩法的贪吃蛇游戏，支持分数记录与难度调节。",
        "prompt": "设计一个 **经典贪吃蛇游戏**，遵循传统贪吃蛇的核心玩法，聚焦游戏体验与交互反馈：\n"
                    "1. 核心游戏机制：\n"
                    "   - 游戏区域：采用**正方形网格画布**（如400x400像素），背景为深色网格，蛇身由连续的彩色方块组成，食物为随机生成的亮色方块（与蛇身颜色区分）；\n"
                    "   - 控制方式：通过**方向键（上/下/左/右）** 控制蛇的移动方向，支持移动端触摸屏幕边缘（上边缘上移、左边缘左移等）操作；\n"
                    "   - 成长与计分：蛇吃到食物后长度增加1节，分数+10分，食物随即在空白区域重新生成，连续吃3个食物后速度提升5%；\n"
                    "   - 失败条件：蛇头碰撞**边界墙壁**或**自身身体**时游戏结束，显示最终得分与历史最高分；\n"
                    "2. 界面与交互：\n"
                    "   - 游戏面板：顶部显示「当前分数」「历史最高分」「当前速度等级」，底部设置「开始/暂停」「重新开始」「难度选择」按钮；\n"
                    "   - 状态反馈：开始前显示「按方向键开始」提示，暂停时覆盖半透明遮罩与「已暂停」文字，游戏结束时弹出结算弹窗（含得分、重新开始按钮）；\n"
                    "   - 难度设置：支持「简单（初始速度慢）」「中等（初始速度中等）」「困难（初始速度快）」三档选择，切换后即时生效；\n"
                    "   - 视觉效果：蛇移动时有轻微位移动画，吃到食物时有粒子爆炸特效，碰撞失败时有闪烁红框警告。"
    },
    {
        "card": {"index": 4},
        "title": "经典俄罗斯方块",
        "description": "还原原版玩法的俄罗斯方块游戏，支持分数记录与级别提升。",
        "prompt": "设计一个 **经典俄罗斯方块**，遵循传统方块消除玩法，核心聚焦方块操作与难度递进：\n"
                    "1. 核心游戏机制：\n"
                    "   - 游戏区域：采用**10x20网格画布**，上方为待下落方块区，底部为已堆积区域，右侧显示下一个方块预览；\n"
                    "   - 控制方式：通过**方向键**操作（左右键移动、上键旋转、下键加速下落、空格键直接落底），支持移动端触摸滑动（左右滑移动、上滑旋转、下滑加速）；\n"
                    "   - 消除与计分：一行填满方块后自动消除，单次消除1行得100分、2行300分、3行500分、4行1000分，分数累积到阈值后提升级别（速度加快）；\n"
                    "   - 失败条件：新方块生成后与已有方块重叠或超出顶部边界时游戏结束，显示最终得分与历史最高分；\n"
                    "2. 界面与交互：\n"
                    "   - 游戏面板：顶部显示「当前分数」「已消行数」「当前级别」，底部设置「开始/暂停」「重新开始」「难度选择」按钮；\n"
                    "   - 状态反馈：暂停时显示半透明遮罩与暂停提示，消除行时有闪烁特效，升级时有短暂的「LEVEL UP」文字动画；\n"
                    "   - 难度设置：初始提供「简单（慢速起步）」「正常（标准速度）」「困难（快速起步）」三档，支持游戏中随分数动态提升速度；\n"
                    "   - 视觉效果：不同形状方块采用鲜明对比色，下落与消除过程有平滑过渡动画，游戏结束时方块区域闪烁红色边框。"
    }
]
    


# DEMO_LIST = [
#   {
#     "card": {
#       "index": 0,
#     },
#     "title": "Qwen，Start！",
#     "description": "Help me design an interface with a purple button that says 'Qwen, Start!'. When the button is clicked, display a countdown from 5 in a very large font for 5 seconds.",
#   },
#   {
#     "card": {
#       "index": 1,
#     },
#     "title": "Spam with emojis!",
#     "description": "Write code in a single HTML file: Capture the click event, place a random number of emojis at the click position, and add gravity and collision effects to each emoji."
#   },
#   {
#     "card": {
#       "index": 2,
#     },
#     "title": "TODO list",
#     "description": "I want a TODO list that allows me to add tasks, delete tasks, and I would like the overall color theme to be purple."
#   },
# ]