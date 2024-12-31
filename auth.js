function login(username, password) {
    if (!username || !password) {
        throw new Error("Username and password are required.");
    }
    // Authenticate user...
    return { token: "some-jwt-token" };
}
