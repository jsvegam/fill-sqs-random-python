# fill-sqs-random-python
fill sqs randomicly with members

# pipeline
# source github
# build skip
# deploy s3
# generate new build project and modify policy to enable to modify de lambda
<!-- ,
        {
            "Effect": "Allow",
            "Action": [
                "lambda:AddPermission",
                "lambda:RemovePermission",
                "lambda:CreateAlias",
                "lambda:UpdateAlias",
                "lambda:DeleteAlias",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:PutFunctionConcurrency",
                "lambda:DeleteFunctionConcurrency",
                "lambda:PublishVersion"
            ],
            "Resource": "arn:aws:lambda:us-east-1:806175290270:function:testpythonapp"
        } -->
