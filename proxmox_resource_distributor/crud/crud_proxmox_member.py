"""Collection of object CRUD classes."""

from typing import List

from proxmoxer import ProxmoxAPI

from proxmox_resource_distributor.crud.base_proxmox import CRUDBaseProxmox
from proxmox_resource_distributor.models import (
    ProxmoxMember as ProxmoxMemberOrm,
)
from proxmox_resource_distributor.schemas import (
    ProxmoxMember as ProxmoxMemberSchema,
)


class CRUDProxmoxMember(
    CRUDBaseProxmox[ProxmoxMemberOrm, ProxmoxMemberSchema]
):
    """CRUD methods for object."""

    def get_by_pool(
        self, proxmox_connection: ProxmoxAPI, pool_name: str
    ) -> List[ProxmoxMemberSchema]:
        """Get object."""
        members = []

        pool = proxmox_connection.pools(pool_name).get()

        for member in pool["members"]:
            members.append(
                ProxmoxMemberSchema(
                    node_name=member["node"],
                    name=member["name"],
                    vm_id=member["vmid"],
                    pool_name=pool_name,
                )
            )

        return members


proxmox_member = CRUDProxmoxMember(ProxmoxMemberOrm, ProxmoxMemberSchema)