/** @type {import('next').NextConfig} */
module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/api/ask",
        destination: `${process.env.BACKEND_URL || 'http://localhost:7860'}/ask`
      },
      {
        source: "/api/podcast",
        destination: `${process.env.BACKEND_URL || 'http://localhost:7860'}/podcast`
      }
    ];
  }
};