/*
   Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   This file is licensed under the Apache License, Version 2.0 (the "License").
   You may not use this file except in compliance with the License. A copy of
   the License is located at
    http://aws.amazon.com/apache2.0/
   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied. See the License for the
   specific language governing permissions and limitations under the License.
*/

package main

import (
    "fmt"

    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/ec2"
)

// Describes the security groups by IDs that are passed into the CLI. Takes
// a space separated list of group IDs as input.
//
func main() {
    // Initialize a session in us-west-2 that the SDK will use to load
    // credentials from the shared credentials file ~/.aws/credentials.
    sess, _ := session.NewSession(&aws.Config{
        Region: aws.String("us-east-1")},
    )

    // Create an EC2 service client.
    svc := ec2.New(sess)

    // Retrieve the security group descriptions
    result, _ := svc.DescribeSecurityGroups(nil)

    fmt.Println("Security Group:")
    for _, group := range result.SecurityGroups {
        fmt.Println(group)
    }
}
