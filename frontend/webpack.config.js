const path = require('path');
const webpack = require('webpack');

const paths = {
    DIST: path.resolve(__dirname, 'dist'),
    SRC: path.resolve(__dirname, 'src'),
    nodeModulesPath: path.resolve(__dirname, 'node_modules')
};

module.exports = {
    entry: {
        // 'react-hot-loader/patch',
        bundle: path.join(paths.SRC, 'app.js'),
    },
    output: {
        path: paths.DIST,
        filename: '[name].js',
        publicPath: '/hotreload/',
    },
    // Dev server configuration -> ADDED IN THIS STEP
    // Now it uses our "src" folder as a starting point
    devServer: {
        contentBase: paths.SRC,
        hot: true,
        host: '0.0.0.0',
        overlay: true,
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: paths.nodeModulesPath,
                use: ['babel-loader']
            },
            {
                test: /\.css$/,
                use: [ 'style-loader', 'css-loader' ]
            }
        ]
    },
};