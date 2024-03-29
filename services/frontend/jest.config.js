module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  setupFiles: ['./tests/unit/setup.js', "jest-canvas-mock"],
  collectCoverage: true,
  collectCoverageFrom: ["**/*.{js,vue}", "!**/node_modules/**"],
  transformIgnorePatterns: [
    "node_modules/(?!echarts|(?!echarts/core))",
  ],
}