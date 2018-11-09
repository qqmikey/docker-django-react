import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';

import * as appReducers from './app/appReducers';

const rootReducer = history => combineReducers({
  router: connectRouter(history),
  ...appReducers,
  // ... rest of your reducers
});

export default rootReducer;
