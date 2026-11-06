# 练习用行程列表；每次创建随机抽取一条，允许重复。预算为模拟值。
trip_samples = [
    {
        "title": "杭州零预算湖畔漫步",
        "destination": "杭州",
        "days": 1,
        "budget": 0,
        "daily_plans": [
            {"day": 1, "morning": "步行到西湖，沿湖观察水鸟", "afternoon": "自带午餐，在树荫下阅读和写生", "evening": "湖边散步后步行回家"}
        ],
    },
    {
        "title": "苏州园林建筑速写",
        "destination": "苏州",
        "days": 1,
        "budget": 400,
        "daily_plans": [
            {"day": 1, "morning": "在拙政园观察窗景与借景构图", "afternoon": "在平江路画一幅街巷速写", "evening": "整理画稿，记录园林建筑细节"}
        ],
    },
    {
        "title": "南京一日游",
        "destination": "南京",
        "days": 1,
        "budget": 350,
        "daily_plans": [
            {"day": 1, "morning": "逛南京博物院", "afternoon": "游玄武湖", "evening": "逛夫子庙"}
        ],
    },
    {
        "title": "上海亲子科普周末：自然探索与星空观察",
        "destination": "上海",
        "days": 2,
        "budget": 2680.5,
        "daily_plans": [
            {"day": 1, "morning": "参观自然博物馆，和孩子寻找恐龙化石", "afternoon": "午休后画出最喜欢的动物，留出自由活动时间", "evening": "一起读自然科普绘本，早点休息"},
            {"day": 2, "morning": "参观天文馆，认识太阳系", "afternoon": "用手工材料制作星球模型", "evening": "分享两天的发现，整理亲子照片"},
        ],
    },
    {
        "title": "北京文化三日游",
        "destination": "北京",
        "days": 3,
        "budget": 2400,
        "daily_plans": [
            {"day": 1, "morning": "参观故宫", "afternoon": "登景山", "evening": "逛王府井"},
            {"day": 2, "morning": "游颐和园", "afternoon": "漫步昆明湖畔", "evening": "品尝北京烤鸭"},
            {"day": 3, "morning": "游天坛", "afternoon": "逛胡同", "evening": "什刹海散步"},
        ],
    },
    {
        "title": "成都茶馆放空两日",
        "destination": "成都",
        "days": 2,
        "budget": 680,
        "daily_plans": [
            {"day": 1, "morning": "睡到自然醒，在住处附近吃早餐", "afternoon": "人民公园喝茶、看书，不安排赶场", "evening": "吃一顿家常川菜后休息"},
            {"day": 2, "morning": "逛社区菜市场", "afternoon": "找安静的茶馆写日记", "evening": "收拾行李，慢慢返程"},
        ],
    },
    {
        "title": "西安历史三日游",
        "destination": "西安",
        "days": 3,
        "budget": 1800,
        "daily_plans": [
            {"day": 1, "morning": "参观陕西历史博物馆", "afternoon": "游大雁塔", "evening": "逛大唐不夜城"},
            {"day": 2, "morning": "参观兵马俑", "afternoon": "游华清宫", "evening": "品尝陕西面食"},
            {"day": 3, "morning": "漫步城墙", "afternoon": "逛碑林博物馆", "evening": "欣赏钟楼夜景"},
        ],
    },
    {
        "title": "厦门海滨两日游",
        "destination": "厦门",
        "days": 2,
        "budget": 1300,
        "daily_plans": [
            {"day": 1, "morning": "游鼓浪屿", "afternoon": "逛岛上街巷", "evening": "漫步中山路"},
            {"day": 2, "morning": "环岛路散步", "afternoon": "海边休息", "evening": "品尝闽南小吃"},
        ],
    },
    {
        "title": "青岛海岸摄影两日",
        "destination": "青岛",
        "days": 2,
        "budget": 1100,
        "daily_plans": [
            {"day": 1, "morning": "在栈桥拍摄晨光与海鸟", "afternoon": "在八大关练习建筑构图", "evening": "拍摄海边日落，备份当天照片"},
            {"day": 2, "morning": "拍摄老城区街巷与生活场景", "afternoon": "在海边练习浪花抓拍", "evening": "挑选十张照片，制作旅行影集"},
        ],
    },
    {
        "title": "长沙美食一日游",
        "destination": "长沙",
        "days": 1,
        "budget": 199.9,
        "daily_plans": [
            {"day": 1, "morning": "游岳麓山", "afternoon": "漫步橘子洲", "evening": "逛坡子街品尝小吃"},
        ],
    },
    {
        "title": "广州风味两日游",
        "destination": "广州",
        "days": 2,
        "budget": 950,
        "daily_plans": [
            {"day": 1, "morning": "体验广式早茶", "afternoon": "参观陈家祠", "evening": "逛北京路"},
            {"day": 2, "morning": "漫步沙面", "afternoon": "参观广东省博物馆", "evening": "欣赏珠江夜景"},
        ],
    },
    {
        "title": "大理五日慢住与白族手作体验",
        "destination": "大理",
        "days": 5,
        "budget": 4800,
        "daily_plans": [
            {"day": 1, "morning": "逛大理古城", "afternoon": "街边喝茶", "evening": "品尝云南菜"},
            {"day": 2, "morning": "洱海边散步", "afternoon": "游喜洲古镇", "evening": "看湖畔日落"},
            {"day": 3, "morning": "前往周城了解扎染工艺", "afternoon": "体验扎染，制作一块手帕", "evening": "记录手作过程"},
            {"day": 4, "morning": "在住处阅读，不安排外出", "afternoon": "村落散步，与同行者喝茶聊天", "evening": "整理旅行照片"},
            {"day": 5, "morning": "到集市选购当地食材", "afternoon": "整理行李和手作纪念品", "evening": "返程"},
        ],
    },
    {
        "title": "莫干山四日轻徒步与山居休息",
        "destination": "浙江德清·莫干山",
        "days": 4,
        "budget": 3200,
        "daily_plans": [
            {"day": 1, "morning": "抵达山下村落", "afternoon": "入住后熟悉周边步道", "evening": "检查天气和次日徒步路线"},
            {"day": 2, "morning": "沿已开放步道轻徒步，观察竹林", "afternoon": "返回住处休息和拉伸", "evening": "记录沿途见到的植物"},
            {"day": 3, "morning": "村落散步，拍摄山间晨景", "afternoon": "在住处看书，雨天也可照常安排", "evening": "与同行者做一顿晚餐"},
            {"day": 4, "morning": "收拾装备，整理徒步记录", "afternoon": "退房返程", "evening": "在家休息"},
        ],
    },
]
