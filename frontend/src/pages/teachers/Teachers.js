export default function Teachers({ username, privilege }) {
    if (!username || !privilege) return <div>unauthorized access</div>

    return <div>Teachers</div>
}