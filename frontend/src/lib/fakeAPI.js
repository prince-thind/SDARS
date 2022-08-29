export async function fetchFakeLoginResponse({ username, password }) {
    const dbUserName1 = "abc"
    const dbPassword1 = "123"

    const dbUserName2 = "abct"
    const dbPassword2 = "123t"

    const dbUserName3 = "abcp"
    const dbPassword3 = "123p"

    if (dbUserName1 === username && dbPassword1 === password) {
        return { exists: true, privilege:"student" };
    }

    if (dbUserName2 === username && dbPassword2 === password) {
        return { exists: true, privilege:"teacher" };
    }

    if (dbUserName3 === username && dbPassword3 === password) {
        return { exists: true, privilege:"parent" };
    }
    return { exists: false }

}