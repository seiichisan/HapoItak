# HapoItak

HapoItak is a web-developr's toolkit that can improve your JAVA, JSP and HTML workflow.
HapoItak parses english reduction expression you type, and produce output JAVA, JSP and HTML code.

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

    property userId ユーザID    

can be expanded into:

    /** ユーザID */
    private String userid;

    /**
     * ユーザIDを取得します。
     * @return ユーザID。
     */
    public String getUserid() {
    	return userid;
    }
    
    /**
     * ユーザIDを設定します。
     * @param userid ユーザID。
     */
    public void setUserid(String userid) {
    	this.userid = userid;
    }
