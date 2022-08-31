export default function Students({ username, privilege }) {
    if (!username || !privilege) return <div>unauthorized access</div>
    return <div>Students</div>


}