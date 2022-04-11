export default function ({ $auth, redirect, store }) {
  console.log($auth.loggedIn);
  if ($auth.loggedIn) {
    return redirect("/home");
  }
  // if (store.state.auth.loggedIn) {
  //   return redirect("/home");
  // }
}
