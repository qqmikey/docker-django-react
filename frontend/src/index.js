import 'react-hot-loader';
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux'

import App from './app/AppContainer';
import { configureStore } from './store/configureStore';
import * as serviceWorker from './serviceWorker';


const mountApp = document.getElementById('root');
const store = configureStore();

function rootRender(Component) {
  if (!mountApp) return null;
  return render(<Provider store={store}><Component /></Provider>, mountApp);
}

rootRender(App);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
