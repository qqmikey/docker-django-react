import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import * as actions from './appActions';
import Component from './AppComponent';

function mapStateToProps(state) {
  return {
    rotation: state.rotationDirection,
    // map other props from state
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(actions, dispatch);
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Component);
