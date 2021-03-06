deployment_json = {
    "apiVersion": "apps/v1beta1",
    "kind": "Deployment",
    "metadata": {
        "name": "sn-collector-deployment"
    },
    "spec": {
        "replicas": 1,
        "template": {
            "metadata": {
                "labels": {
                    "app": "sn-collector",
                    "tenant": ""
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "sn-collector-ctr",
                        "image": "alpine/sn-collector:2.0",
                        "env": [
                            {
                                "name": "configs",
                                "value": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
}
