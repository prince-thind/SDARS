import { useState } from "react";
import { submitProgress } from "../../../lib/API";
import Error from "../../../lib/commonComponents/ErrorToast";

export default function ProgressSection() {
    const [error, setError] = useState(null)
    const [res, setRes] = useState(null)

    return <form className="form module" onSubmit={handleSubmit}>
        <h3>Upload Progress report</h3>
        <div className="container">
            <label>Enter Username: <input type="text" required name="username"></input> </label>
            <label>Enter Subject Name: <input type="text" required name="subject-name"></input> </label>
            <label>Enter Max Marks: <input type="number" required name="max-marks" value="100"></input> </label>
            <label>Enter Marks Obtained: <input type="number" required name="marks-obtained" value="0"></input> </label>
            <label>Enter description: <input type="text" name="description" value="N/A"></input> </label>
        </div>
        <button>Submit</button>
        {error && <Error error={error} />}
        {res && <div className="success">{res}</div>}
    </form>;

    async function handleSubmit(e) {
        e.preventDefault();
        setRes(null)
        setError(null)
        const form = e.target;
        const values = Object.fromEntries(new FormData(form).entries())

        const status = await submitProgress(values);
        if (status) {
            setRes('Uploaded')
        }
        else {
            setError('Error Uploading')
        }

    }
}

