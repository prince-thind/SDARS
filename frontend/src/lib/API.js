import customFetch from "./customFetch";

export async function login({ username, password, setUsername, navigate, setPrivilege, setUserClass }) {
    const response = await customFetch('/login/', { method: 'POST', body: { username, password } });

    if (!response.exists) {
        setUsername(null);
        navigate("/login")
        return { error: "Username or Password incorrect" }
    }

    setUsername(username);
    const { privilege, userClass } = response;
    setPrivilege(privilege);
    setUserClass(userClass);

    switch (privilege) {
        case "student": navigate("/students");
            break;
        case "teacher": navigate("/teachers");
            break;
        case "parent": navigate("/parents");
            break;
        default: navigate("/login")
    }

    return { error: null };
}

export async function fetchCirculars() {
    return (await customFetch("/students/circulars/")).data;
}

export async function fetchResults(username) {
    return (await customFetch("/students/results/"+username)).data;
}

export async function fetchAssignments(userClass) {
    return (await customFetch("/students/assignments/"+userClass)).data;

}

export async function fetchProgress(username) {
    return (await customFetch("/students/progress/"+username)).data;

}

export async function fetchAttedence(username) {
    return (await customFetch("/students/attendence/"+username)).data;

}

export async function fetchParentsProgress(username) {
    return (await customFetch("/parents/progress/"+username)).data;

}

export async function fetchParentsAttendence(username) {
    return (await customFetch("/parents/attedence/"+username)).data;

}

export async function fetchFees(username) {
    return (await customFetch("/parents/fees/"+username)).data;

}

export async function submitProgress(data) {
    return (await customFetch('/teachers/progress/', { method: 'POST', body: { data } })).status;
}

export async function submitAttedence(data) {
    return (await customFetch('/teachers/attedence/', { method: 'POST', body: { data } })).status;

}

export async function submitAssignment(data) {
    return (await customFetch('/teachers/assignment/', { method: 'POST', body: { data } })).status;

}


export async function submitResult(data) {
    return (await customFetch('/teachers/result/', { method: 'POST', body: { data } })).status;

}

