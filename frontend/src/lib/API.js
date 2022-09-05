import { fetchFakeCirculars, fetchFakeLoginResponse, fetchFakeResults } from "./fakeAPI";

export async function login({ username, password, setUsername, navigate, setPrivilege }) {
    const response = await fetchFakeLoginResponse({ username, password });

    if (!response.exists) {
        setUsername(null);
        navigate("/login")
        return
    }

    setUsername(username);
    const { privilege } = response;
    setPrivilege(privilege);
    switch (privilege) {
        case "student": navigate("/students");
            break;
        case "teacher": navigate("/teachers");
            break;
        case "parent": navigate("/parents");
            break;
        default: navigate("/login")
    }

}

export async function fetchCirculars() {
    return (await fetchFakeCirculars()).data;
}

export async function fetchResults(username) {
    return (await fetchFakeResults(username)).data;
}