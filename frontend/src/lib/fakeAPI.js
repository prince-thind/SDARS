export async function fetchFakeLoginResponse({ username, password }) {
    const dbUserName1 = "abc"
    const dbPassword1 = "123"

    const dbUserName2 = "abct"
    const dbPassword2 = "123t"

    const dbUserName3 = "abcp"
    const dbPassword3 = "123p"

    if (dbUserName1 === username && dbPassword1 === password) {
        return { exists: true, privilege: "student" };
    }

    if (dbUserName2 === username && dbPassword2 === password) {
        return { exists: true, privilege: "teacher" };
    }

    if (dbUserName3 === username && dbPassword3 === password) {
        return { exists: true, privilege: "parent" };
    }
    return { exists: false }

}


export async function fetchFakeCirculars() {

    await sleep(1);

    return {
        data: [{
            name: "Updated Library Timings",
            description: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent elementum mauris risus, non tincidunt enim semper sit amet. Donec fermentum et leo et mattis. Nunc feugiat dolor finibus massa facilisis bibendum. Donec pellentesque vulputate elit et auctor. Vivamus maximus tellus et magna molestie tristique. Donec sed augue sodales, elementum elit sit amet, feugiat lectus. Maecenas molestie quam eget ipsum viverra placerat. Ut porta sollicitudin justo in pharetra. Donec laoreet imperdiet sapien. Aenean imperdiet iaculis ante non placerat. Aenean tristique accumsan placerat. Suspendisse potenti. Morbi tellus justo, mattis sit amet augue quis, suscipit pretium enim.`,
            date: new Date(new Date().setDate(1)).toISOString(),
            id: 0,
        }, {
            name: "Holiday",
            description: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent elementum mauris risus, non tincidunt enim semper sit amet. Donec fermentum et leo et mattis. Nunc feugiat dolor finibus massa facilisis bibendum. Donec pellentesque vulputate elit et auctor. Vivamus maximus tellus et magna molestie tristique. Donec sed augue sodales, elementum elit sit amet, feugiat lectus. Maecenas molestie quam eget ipsum viverra placerat. Ut porta sollicitudin justo in pharetra. Donec laoreet imperdiet sapien. Aenean imperdiet iaculis ante non placerat. Aenean tristique accumsan placerat. Suspendisse potenti. Morbi tellus justo, mattis sit amet augue quis, suscipit pretium enim.`,
            date: new Date().toISOString(),
            id: 1,
        }]
    }
}


export async function fetchFakeResults(username) {
    await sleep(1);
    return {
        data: [
            { name: 'test1', maxMarks: 100, marksGot: 75, type: 'classTest', id: 0 },
            { name: 'test2', maxMarks: 100, marksGot: 85, type: 'unit test', id: 1 },
        ]
    }
}

export async function fetchFakeAssignments() {
    await sleep(1);
    return {
        data: [
            { name: 'assignment1', maxMarks: 100, description: "lorem lorem blha blha", dueDate: new Date().toISOString(), id: 0 },
            { name: 'assignment2', maxMarks: 100, description: "lorem lorem blha blha2", dueDate: new Date().toISOString(), id: 1 },
        ]
    }
}

export async function fetchFakeProgress(username) {
    await sleep(1);
    return {
        data: [
            { name: 'subject1', grade: 'A', description: "lorem lorem blha blha", id: 0 },
            { name: 'subject2', grade: 'A+', description: "lorem lorem blha blha2", id: 1 },
        ]
    }
}
export async function fetchFakeAttendence(username) {
    await sleep(1);
    return {
        data: [
            { name: username, remarks: "lorem lorem blha blha", attendence: 95 },
        ]
    }
}

export async function fetchFakeFees(parentName) {
    await sleep(1);
    return {
        data: [
            { name: 'trip charges', cost: 450, description: "lorem lorem blha blha", id: 0 },
            { name: 'tution fees', cost: 1500, description: "lorem lorem blha blha2", id: 1 },
        ]
    }
}

function sleep(n) {
    return new Promise(r => setTimeout(r, n * 1000))
}
