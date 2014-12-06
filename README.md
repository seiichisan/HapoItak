# HapoItak

HapoItak is a web-developr's toolkit that can improve your JAVA, JSP and HTML workflow.
HapoItak parses english reduction expression you type, and produce output JAVA, JSP and HTML code.

Homepage is [HapoItak](https://tolemy.sakura.ne.jp/)

## Example 1
For example, In the file by which an extension is jsp, this reduction expression:

    jsf if

can be expanded into:

    <c:if test='${xxx == "y"}'>
    
    </c:if>

## Example 2
For example, In the file by which an extension is jsp, this reduction expression:

    jsf if else

can be expanded into:

    <c:if test='${xxx == "y"}'>
    
    </c:if>
    <c:if test='${xxx != "y"}'>
    
    </c:if>

## Example 3
For example, In the file by which an extension is java, this reduction expression:

    property user_id ユーザID

can be expanded into:

    /** ユーザID */
    private String userId;

    /**
     * ユーザIDを取得します。
     * @return ユーザID。
     */
    public String getUserId() {
        return userId;
    }

    /**
     * ユーザIDを設定します。
     * @param userId ユーザID。
     */
    public void setUserId(String userId) {
        this.userId = userId;
    }
