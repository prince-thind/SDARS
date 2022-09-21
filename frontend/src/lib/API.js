import { fetchFakeAssignments, fetchFakeAttendence, fetchFakeCirculars, fetchFakeFees, fetchFakeLoginResponse, fetchFakeProgress, fetchFakeResults, submitFakeAssignment, submitFakeAttedence, submitFakeProgress } from "./fakeAPI";

export async function login({ username, password, setUsername, navigate, setPrivilege }) {
    const response = await fetchFakeLoginResponse({ username, password });

    if (!response.exists) {
        setUsername(null);
        navigate("/login")
        return {error: "Username or Password incorrect"}
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

    return null;
}

export async function fetchCirculars() {
    return (await fetchFakeCirculars()).data;
}

export async function fetchResults(username) {
    return (await fetchFakeResults(username)).data;
}

export async function fetchAssignments(username) {
    return (await fetchFakeAssignments(username)).data;
}

export async function fetchProgress(username) {
    return (await fetchFakeProgress(username)).data;
}

export async function fetchAttedence(username) {
    return (await fetchFakeAttendence(username)).data;
}

export async function fetchParentsProgress(username) {
    return (await fetchFakeProgress(username)).data;
}

export async function fetchParentsAttendence(username) {
    return (await fetchFakeAttendence(username)).data;
}

export async function fetchFees(parentName) {
    return (await fetchFakeFees(parentName)).data;
}

export async function submitProgress(data) {
    return (await submitFakeProgress(data)).status;
}

export async function submitAttedence(data) {
    return (await submitFakeAttedence(data)).status;
}

export async function submitAssignment(data) {
    return (await submitFakeAssignment(data)).status;
}

