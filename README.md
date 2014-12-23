# HapoItak

HapoItak is a web-developr's powerful toolkit that can improve your HTML, JSP and JAVA workflow.
HapoItak adds aditional auto-completion capability to edit file of HTML, JSP AND JAVA. The code longer than usual can be able to complemented by HapoItak.

And also, HapoItak has some conversion function.
For example, HapoItak adds comma to each word and wrap each word with double quotation.

And also, HapoItak parses english reduction expression you type, and produce output JAVA.

Homepage is [HapoItak](https://tolemy.sakura.ne.jp/)

## Example 1
HapoItak adds comma to each word and wrap each word with double quotation by 'ctrl+alt+u' key input.

Before  
![before and after 1](https://tolemy.sakura.ne.jp/img/17_double_quotation_1.JPG)

After No.1  
![before and after 2](https://tolemy.sakura.ne.jp/img/18_double_quotation_2.JPG)

After No.2  
![before and after 3](https://tolemy.sakura.ne.jp/img/19_double_quotation_3.JPG)


## Example 2
The text is surrounded with html tag by 'ctrl+alt+n' key input by HapoItak.
The text can be able to surrounded with html tag every line.

Before  
![before and after 4](https://tolemy.sakura.ne.jp/img/14_encirclement_br_before_1.JPG)

After No.1  
![before and after 5](https://tolemy.sakura.ne.jp/img/15_encirclement_br_after_2.JPG)

After No.2  
![before and after 6](https://tolemy.sakura.ne.jp/img/16_encirclement_br_after_3.JPG)


## Example 3
HapoItak replace html special character with html entities by 'ctrl+alt+y' key input.

Before  
![before and after 10](https://tolemy.sakura.ne.jp/img/01_beforeSpecialReplace.JPG)

After  
![before and after 11](https://tolemy.sakura.ne.jp/img/02_afterSpecialReplace.JPG)

## Example 4
HapoItak escape double quotation by 'ctrl+alt+h' key input.

Before  
![before and after 12](https://tolemy.sakura.ne.jp/img/03_beforeEscapeDoubleQ.JPG)

After  
![before and after 13](https://tolemy.sakura.ne.jp/img/04_afterEscapeDoubleQ.JPG)

## Example 5
For example, the following list is shown to input which is 'jsf'.

1. jsf_if_a=b
2. jsf_if_a=b_else
3. jsf_hidden
4. jsf_commandButton
5. jsf_outputText

For example, 'jsf_if_a=b' expression is expanded into:

    <c:if test='${$1 == "$2"}'>
    $3
    </c:if>

For example, 'jsf_if_a=b_else' expression is expanded into:

    <c:if test='${$1 == "$2"}'>
    $3
    </c:if>
    <c:if test='${$4 != "$5"}'>
    $6
    </c:if>

## Example 6
For example, In the file by which an extension is java, this reduction expression:

    property user_id ユーザID

can be expanded by into:

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

Operation above-mentioned is performed by 'ctrl+i'.

