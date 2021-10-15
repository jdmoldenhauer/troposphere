# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 43.1.0


from troposphere import Tags

from . import AWSObject, AWSProperty


class PreloadDataConfig(AWSProperty):
    props = {
        "PreloadDataType": (str, True),
    }


class KmsEncryptionConfig(AWSProperty):
    props = {
        "CmkType": (str, True),
        "KmsKeyId": (str, False),
    }


class SseConfiguration(AWSProperty):
    props = {
        "KmsEncryptionConfig": (KmsEncryptionConfig, True),
    }


class FHIRDatastore(AWSObject):
    resource_type = "AWS::HealthLake::FHIRDatastore"

    props = {
        "DatastoreName": (str, False),
        "DatastoreTypeVersion": (str, True),
        "PreloadDataConfig": (PreloadDataConfig, False),
        "SseConfiguration": (SseConfiguration, False),
        "Tags": (Tags, False),
    }