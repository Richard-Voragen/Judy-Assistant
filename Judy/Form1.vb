Public Class Form1

    Dim Num01 As String = Nothing
    Dim Objct As String = Nothing
    Dim Num02 As String = Nothing
    Dim answer As String = Nothing

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged

    End Sub

    Private Sub TextBox2_TextChanged(sender As Object, e As EventArgs) Handles TextBox2.TextChanged

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If TextBox1.Text = "Hi" Then
            TextBox2.Text = "Hello"
        ElseIf TextBox1.Text = "Hello" Then
            TextBox2.Text = "Hi"
        ElseIf TextBox1.Text = ".cal" Then
            TextBox2.Text = "What is your first number?"
        ElseIf TextBox2.Text = "What is your first number?" Then
            TextBox1.Text = Num01
            TextBox2.Text = "+ - * /"
        ElseIf TextBox2.Text = "+ - * /" Then
            TextBox1.Text = Objct
            TextBox2.Text = "What is your last number?"
        ElseIf TextBox2.Text = "What is your last number?" Then
            TextBox1.Text = Num02
            answer = Num01 + Objct + Num02

        End If



    End Sub
End Class
