import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
// eslint-disable-next-line import/no-extraneous-dependencies
import { createBrowserHistory } from 'history';
import { routerMiddleware } from 'connected-react-router';
// eslint-disable-next-line import/no-extraneous-dependencies
// import { persistState } from 'redux-devtools';

import createRootReducer from '../rootReducer';
// import type { counterStateType } from '../reducers/types';

import DevTools from '../reduxDevTools/DevTools';


// function getDebugSessionKey() {
//   // You can write custom logic here!
//   // By default we try to read the key from ?debug_session=<key> in the address bar
//   const matches = window.location.href.match(/[?&]debug_session=([^&]+)\b/);
//   return (matches && matches.length > 0) ? matches[1] : null;
// }

// const history = createHashHistory();
const history = createBrowserHistory();
const router = routerMiddleware(history);
const enhancer = compose(
  applyMiddleware(thunk, router),
  DevTools.instrument(),
  // Optional. Lets you write ?debug_session=<key> in address bar to persist debug sessions
  // persistState(getDebugSessionKey()),
);

// function configureStore(initialState?: counterStateType) {
//     return createStore(rootReducer, initialState, enhancer);
// }

function configureStore(initialState) {
  const store = createStore(createRootReducer(history), initialState, enhancer);

  // Hot reload reducers (requires Webpack or Browserify HMR to be enabled)
  if (module.hot) {
    module.hot.accept('../rootReducer',
      // eslint-disable-next-line global-require
      () => store.replaceReducer(require('../rootReducer') /* .default if you use Babel 6+ */));
  }

  return store;
}

export default {
  configureStore,
  history
};
