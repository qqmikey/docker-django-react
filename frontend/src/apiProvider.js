// @flow
import Requests from './utils/Requests';


const ENDPOINT = 'http://localhost';
const API = `${ENDPOINT}/api/v1/`;

class ApiProvider {
  _instance = null;
  r: Requests;

  /**
   * @return {null}
   */
  constructor() {
    if (!this._instance) {
      this._instance = this;
      this.r = new Requests({ 'Content-Type': 'application/json', 'Accept': 'application/json' });
    }
    return this._instance;
  }

  async fetchProfile() {
    const response = await this.r.fetch(`${API}profile`);
    if (response.ok) return response.json();
    return null;
  }
}

export default new ApiProvider();
