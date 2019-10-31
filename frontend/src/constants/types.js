// @flow

export type actionType = {
  +type: string,
  +payload?: any
};

export type dispatchType = (action: actionType) => void;
