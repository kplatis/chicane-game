const withBundleAnalyzer = require('@next/bundle-analyzer')({
    enabled: process.env.ANALYZE === 'true',
});

const path = require('path');
  
module.exports = withBundleAnalyzer({
    reactStrictMode: false,
    eslint: {
        ignoreDuringBuilds: true,
    },
    pageExtensions: ['js', 'jsx', 'ts', 'tsx'], 
    pagePath: path.join(__dirname, 'src', 'pages'),  
});
  