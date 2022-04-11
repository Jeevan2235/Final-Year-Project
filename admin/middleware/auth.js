export default function ({ store, redirect }) {
  console.log("AUTH PAGE--------------------------");
  if (!$auth.loggedIn) {
    return redirect("/login");
  }
}
