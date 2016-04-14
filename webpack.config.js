var path = require('path');
var src = path.resolve(__dirname, 'client');
var dist = path.resolve(__dirname, 'static');

var config = {
  entry: path.resolve(src, 'main.js'),
  devtool: 'source-map',
  output: {
    path: dist,
    filename: 'todomvc.js'
  },
  module: {
    loaders: [{
      test: /\.css$/,
      loader: 'style!css'
    }, {
      test: /\.js?$/,
      loader: 'babel',
      include: src,
      query: {
          cacheDirectory: true,
          presets: ['es2015', 'react'],
          plugins: ['transform-decorators-legacy']
      }

    }]
  },
  resolve: {
    extensions: ['', '.js', '.jsx'],
    fallback: path.join(__dirname, 'node_modules')
  },

  resolveLoader: {
    root: path.join(__dirname, 'node_modules')
  }
};

module.exports = config;
