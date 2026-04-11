from enum import Enum

class Region(Enum):
    I = 1
    II = 2
    III = 3
    IV = 4

regional_min_salary = {
    Region.I: 5310000,
    Region.II: 4730000,
    Region.III: 4140000,
    Region.IV: 3700000,
}

MAX_INT = 2**64 - 1
MAX_DEPENDENTS = 10

BASE_SALARY = 2340000
SELF_DEDUCTION = 15500000
DEPENDENT_DEDUCTION = 6200000

def gross_to_net(
    gross_salary: int, dependents_count: int, insurance_salary: int, region: Region
) -> int:
    if not (
        0 <= gross_salary <= MAX_INT
        and 0 <= dependents_count <= MAX_DEPENDENTS
        and regional_min_salary[region] <= insurance_salary <= MAX_INT
        and region in regional_min_salary
    ):
        raise ValueError("Invalid input")

    social_insurance = 0.08 * min(20 * BASE_SALARY, insurance_salary)
    health_insurance = 0.015 * min(20 * BASE_SALARY, insurance_salary)
    unemployment_insurance = 0.01 * min(
        20 * regional_min_salary[region], insurance_salary
    )

    total_insurance = social_insurance + health_insurance + unemployment_insurance

    total_deduction = SELF_DEDUCTION + DEPENDENT_DEDUCTION * dependents_count

    taxable_salary = max(0, gross_salary - total_insurance - total_deduction)

    print(taxable_salary)
    total_tax = 0
    if taxable_salary > 0:
        total_tax += 0.05 * (min(taxable_salary, 10000000))
    if taxable_salary > 10000000:
        total_tax += 0.1 * (min(taxable_salary, 30000000) - 10000000)
    if taxable_salary > 30000000:
        total_tax += 0.2 * (min(taxable_salary, 60000000) - 30000000)
    if taxable_salary > 60000000:
        total_tax += 0.3 * (min(taxable_salary, 100000000) - 60000000)
    if taxable_salary > 100000000:
        total_tax += 0.35 * (taxable_salary - 100000000)

    return round(gross_salary - total_insurance - total_tax)

if __name__ == "__main__":
    gross = 130_000_000
    dep = 2 
    region = Region.III
    ins = regional_min_salary[region]
    print(f"ins: {ins}")
    print(gross_to_net(gross, dep, ins, region))
    