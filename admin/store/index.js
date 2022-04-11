export const state = () => ({
  endpoint: "",
  limit: 10,
  page: 1,
});

export const getters = {
  getEndpoint(state) {
    return state.endpoint;
  },
  getLimit(state) {
    return state.limit;
  },

  getPage(state) {
    return state.page;
  },
};

export const mutations = {
  setEndpoint(state, payload) {
    state.endpoint = payload;
  },
  setLimit(state, payload) {
    state.limit = payload;
  },

  setPage(state, payload) {
    state.page = payload;
  },
};
