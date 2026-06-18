

# AUTHENTICATION ROUTES (uncomment when needed)
# @router.post("/login")
# def login_user(
#    email: str,
#    password: str,
#    db: Annotated[Session, Depends(get_db)]
# ):
#    """Authenticate user and return session token"""
#    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
#    if not user:
#       raise HTTPException(status_code=401, detail="Invalid credentials")
#    
#    # TODO: Verify hashed password
#    # if not pwd_context.verify(password, user.password):
#    if user.password != password:
#       raise HTTPException(status_code=401, detail="Invalid credentials")
#    
#    # TODO: Generate JWT token or session ID
#    # session_id = str(uuid.uuid4())
#    # return {"session_id": session_id, "user": user}
#    return {"message": "Login successful", "user_id": user.id}
#
# @router.post("/logout")
# def logout_user():
#    """Logout user and invalidate session"""
#    # TODO: Invalidate session/token in cache or database
#    return {"message": "Logged out successfully"}
#
# def get_session_id(session_id: Optional[str] = Cookie(None)):
#    """Starts the session to identify with the users' browser"""
#    if not session_id:
#       session_id = str(uuid.uuid4())
#    return session_id
