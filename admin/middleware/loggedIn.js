export default function ({ $auth, redirect }) {
  console.log("logged in PAGE--------------------------");
  console.log($auth.loggedIn);
  if ($auth.loggedIn) {
    return redirect("/");
  }
}
