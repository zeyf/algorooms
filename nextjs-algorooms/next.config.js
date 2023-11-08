/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'lh3.googleusercontent.com',
        pathname: '/a/**',
      },
    ],
  },
  env: {
    LB_PUBLIC_API_KEY: "pk_dev_7rSbiCxmktdPPA-hgYZsTSxKsm3d3WUtHWKcq8wYTBLEV6lJKnWHGmEkZzEGsfMS",
    EXEC_CLIENT_ID: "1bdc00313dce23b638ba46eb66716718",
    EXEC_CLIENT_SECRET: "c1cd2afd62d64426a3ddc9183ff7a470c7b8136cf682772177dd37ee9bbd9550"
  }
};

module.exports = nextConfig;
