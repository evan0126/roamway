import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // 允许通过这个局域网地址访问开发资源
  allowedDevOrigins: ["192.168.0.83"],
};

export default nextConfig;
