import config from "../config";
import { fetchFakeAssignments, fetchFakeAttendence, fetchFakeCirculars, fetchFakeFees, fetchFakeLoginResponse, fetchFakeProgress, fetchFakeResults, submitFakeAssignment, submitFakeAttedence, submitFakeProgress, submitFakeResult } from "./fakeAPI";

const origin = config.origin;

export default async function customFetch(route, config) {
    if (!origin) return await fakeFetch(route, config);

    if (config.method === 'GET') {
        return await fetch(origin + route);
    }
    else {
        return await fetch(origin, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(config.body)
        })
    }
}

async function fakeFetch(route, postData) {
    switch (route) {
        case '/login/': return fetchFakeLoginResponse({ username: postData.body.username, password: postData.body.password });

        case '/students/circulars/':
        case '/teachers/circulars/':
        case '/parents/circulars/': return fetchFakeCirculars();

        case '/teachers/results/': return submitFakeResult({});

        case '/teachers/assignments/': return submitFakeAssignment({});

        case '/teachers/progress/': return submitFakeProgress({})

        case '/teachers/attendence/': return submitFakeAttedence({})
        case '/parents/attendence/{username}': return null;

        case '/parents/fees/{username}': return null;
        default: return fetchMethods();
    }

    function fetchMethods() {
        if (route.includes('/students/results/')) {
            return fetchFakeResults()
        };

        if (route.includes('/students/assignments/')) {
            return fetchFakeAssignments()
        };

        if (route.includes('/students/progress/')) {
            return fetchFakeProgress()
        };

        if (route.includes('/parents/progress/')) {
            return fetchFakeProgress()
        };

        if (route.includes('/students/attendence/')) {
            return fetchFakeAttendence()
        };

        if (route.includes('/parents/attendence/')) {
            return fetchFakeAttendence()
        };

        if (route.includes('/parents/fees/')) {
            return fetchFakeFees()
        };

    }
}