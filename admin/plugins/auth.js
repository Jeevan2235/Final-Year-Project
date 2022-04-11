export default ({ app }) => {
  // Only _actual_ login/outs (including resets) will be watched here.
  app.$auth.watchState("loggedIn", (isLoggedIn) => {
    if (isLoggedIn) {
      // Follow @nuxtjs/auth workflow.
      app.$auth.redirect("/");
    }
  });
};
