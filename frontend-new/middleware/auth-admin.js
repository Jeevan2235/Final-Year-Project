export default function ({ $auth, redirect, store }) {
  if (!($auth.loggedIn && $auth.user.role === "STAFF")) {
    return redirect("/signup");
  }
}
