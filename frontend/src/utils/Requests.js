// @flow
import queryString from 'query-string';

import { objectFilter, objectMap } from './common';


type objType = { [key: string]: any };

export function createUrlString(url: string, queryParams: ?string | objType): string {
  const params = queryParams instanceof Object ? objectToQueryParametersString(queryParams) : queryParams;
  if (!params) return url;
  return url + (url.includes('?') ? '&' : '?') + params.toString();
}

export default class Requests {
  static GET = 'GET';
  static POST = 'POST';
  static PATCH = 'PATCH';

  headers: ? { [key: string]: string };

  constructor(headers?: HeadersInit) {
    this.headers = headers ? headersToObj(headers) : undefined;
  }

  fetch(url: string, options?: RequestOptions, queryParameters?: ?string | objType) {
    const _url = createUrlString(url, queryParameters);
    const init = options || {};
    const headers = this.getHeaders(init.headers);
    if (headers) init.headers = headers;
    return fetch(_url, init);
  }

  getHeaders(headers?: ?HeadersInit): ?HeadersInit {
    if (!this.headers) return headers;
    if (!headers) return this.headers;
    const h = headersToObj(headers);
    return { ...this.headers, ...h };
  }
}

export function objectToQueryParametersString(obj: objType): ?string {
  if (!obj) return null;
  let params = objectFilter(obj, (value) => value != null && !Number.isNaN(value));
  params = objectMap(params, (val) => {
    if (val instanceof Date) return val.toISOString();
    return val;
  });
  if (Object.keys(params).length === 0) return null;
  return queryString.stringify(params);
}

export function headersToObj(headers: HeadersInit): { [key: string]: string } {
  if (headers instanceof Headers) {
    const obj = {};
    for (const [key, value] of headers) {
      obj[key] = value;
    }
    return obj;
  }
  return headers;
}
