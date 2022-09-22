import { useState } from "react";
import { submitAssignment } from "../../../lib/API";
import Error from "../../../lib/commonComponents/ErrorToast";

export default function AssignmentSection() {
    const [error, setError] = useState(null)
    const [res, setRes] = useState(null)

    return <form className="form module" onSubmit={handleSubmit}>
        <h3>Upload Assignment</h3>
        <div className="container">
            <label>Upload File: <input type="file" name="file"></input> </label>
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
        const file = form.file.files[0];
        const text = (await (file.text()))
        const values = { text, file }

        const status = await submitAssignment(values);
        if (status) {
            setRes('Uploaded')
        }
        else {
            setError('Error Uploading')
        }

    }
}

