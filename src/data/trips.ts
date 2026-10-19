export type DailyPlan = {
  day: number;
  morning: string;
  afternoon: string;
  evening: string;
};

type Trip = {
  id: string;
  title: string;
  content: string;
  dailyPlans: DailyPlan[];
};

export const trips: Trip[] = [
  {
    id: "1",
    title: "杭州三日游",
    content: "这是一个关于杭州三日游的详细行程安排。",
    dailyPlans: [
      {
        day: 1,
        morning: "游览西湖",
        afternoon: "参观雷峰塔",
        evening: "逛河坊街",
      },
      {
        day: 2,
        morning: "参观灵隐寺",
        afternoon: "游览龙井村",
        evening: "湖滨散步",
      },
      {
        day: 3,
        morning: "游览西溪湿地",
        afternoon: "购买伴手礼",
        evening: "返程",
      },
    ],
  },
  {
    id: "2",
    title: "成都五日游",
    content: "这是一个关于成都五日游的详细行程安排。",
    dailyPlans: [],
  },
];