export default function Parents({ username, privilege }) {
    if (!username || !privilege) return <div>unauthorized access</div>

    return <div>parents</div>
}