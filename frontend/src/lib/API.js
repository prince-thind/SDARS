import { fetchFakeLoginResponse } from "./fakeAPI";

export async function login({ username, password, setUsername, navigate }) {
    const response = await fetchFakeLoginResponse({ username, password });

    if (!response.exists) {
        setUsername(null);
        navigate("/login")
        return
    }
    
    setUsername(username);
    const { privilege } = response;
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