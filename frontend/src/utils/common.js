// @flow

type objType = { [key: string]: any };
type objMapFn = (value: any, key?: string, object?: objType) => any;
type objFilterFn = (value: any, key?: string, object?: objType) => boolean;

export function objectMap(object: objType, mapFn: objMapFn, initialValue?: objType): objType {
  return Object.keys(object).reduce((result, key) => {
    // eslint-disable-next-line no-param-reassign
    result[key] = mapFn(object[key], key, object);
    return result;
  }, initialValue || {});
}

export function objectFilter(object: objType, filterFn: objFilterFn, initialValue?: objType): objType {
  return Object.keys(object).reduce((result, key) => {
    const value = object[key];
    if (filterFn(value, key, object)) result[key] = value;
    return result;
  }, initialValue || {});
}

export function withTimeout<T>(promise: Promise<T>, timeout: number): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    let isDone = false;
    let cancelTimeout: ?((val: any) => void) => (val: any) => void;
    if (timeout) {
      const timeoutId = setTimeout(() => {
        if (isDone) return;
        isDone = true;
        reject(new Error("timeout"));
      }, timeout);

      cancelTimeout = (callback) => (value) => {
        if (isDone) return;
        isDone = true;
        clearTimeout(timeoutId);
        callback(value);
      };
    }
    promise
      .then(cancelTimeout ? cancelTimeout(resolve) : resolve)
      .catch(cancelTimeout ? cancelTimeout(reject) : reject);
  });
}
