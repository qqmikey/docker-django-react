const path = require('path');

const dirname = path.join(__dirname, '..');
const paths = {
  appSrc: path.resolve(dirname, 'src'),
  output: path.resolve(dirname, 'dist'),
  publicPath: '/static/dist/',
  nodeModulesPath: path.resolve(dirname, 'node_modules'),

};

module.exports = paths;
