from typing import Any, Dict, List, Optional

from mlflow.entities._mlflow_object import _MlflowObject
from mlflow.entities.assessment import Assessment
from mlflow.entities.metric import Metric


class Evaluation(_MlflowObject):
    """
    Evaluation result data.
    """

    def __init__(
        self,
        evaluation_id: str,
        run_id: str,
        inputs_id: str,
        inputs: Dict[str, Any],
        outputs: Optional[Dict[str, Any]] = None,
        request_id: Optional[str] = None,
        targets: Optional[Dict[str, Any]] = None,
        assessments: Optional[List[Assessment]] = None,
        metrics: Optional[List[Metric]] = None,
        error_code: Optional[str] = None,
        error_message: Optional[str] = None,
    ):
        """
        Construct a new mlflow.entities.Evaluation instance.

        Args:
            evaluation_id: A unique identifier for the evaluation result.
            run_id: The ID of the MLflow Run containing the Evaluation.
            inputs_id: A unique identifier for the input names and values for evaluation.
            inputs: Input names and values for evaluation.
            outputs: Outputs obtained during inference.
            request_id: The ID of an MLflow Trace corresponding to the inputs and outputs.
            targets: Expected values that the model should produce during inference.
            assessments: Assessments for the given row.
            metrics: Objective numerical metrics for the row, e.g., "number of input tokens",
                "number of output tokens".
            error_code: An error code representing any issues encountered during the evaluation.
            error_message: A descriptive error message representing any issues encountered during
                the evaluation.
        """
        self._evaluation_id = evaluation_id
        self._run_id = run_id
        self._inputs_id = inputs_id
        self._inputs = inputs
        self._outputs = outputs
        self._request_id = request_id
        self._targets = targets
        self._assessments = assessments
        self._metrics = metrics
        self._error_code = error_code
        self._error_message = error_message

    @property
    def evaluation_id(self) -> str:
        """Get the evaluation ID."""
        return self._evaluation_id

    @property
    def run_id(self) -> str:
        """Get the run ID."""
        return self._run_id

    @property
    def inputs_id(self) -> str:
        """Get the inputs ID."""
        return self._inputs_id

    @property
    def inputs(self) -> Dict[str, Any]:
        """Get the inputs."""
        return self._inputs

    @property
    def outputs(self) -> Optional[Dict[str, Any]]:
        """Get the outputs."""
        return self._outputs

    @property
    def request_id(self) -> Optional[str]:
        """Get the request ID."""
        return self._request_id

    @property
    def targets(self) -> Optional[Dict[str, Any]]:
        """Get the targets."""
        return self._targets

    @property
    def assessments(self) -> Optional[List[Assessment]]:
        """Get the assessments."""
        return self._assessments

    @property
    def metrics(self) -> Optional[List[Metric]]:
        """Get the metrics."""
        return self._metrics

    @property
    def error_code(self) -> Optional[str]:
        """Get the error code."""
        return self._error_code

    @property
    def error_message(self) -> Optional[str]:
        """Get the error message."""
        return self._error_message

    def __eq__(self, __o):
        if isinstance(__o, self.__class__):
            return self.to_dictionary() == __o.to_dictionary()

        return False

    def to_dictionary(self) -> Dict[str, Any]:
        """
        Convert the Evaluation object to a dictionary.

        Returns:
            dict: The Evaluation object represented as a dictionary.
        """
        evaluation_dict = {
            "evaluation_id": self.evaluation_id,
            "run_id": self.run_id,
            "inputs_id": self.inputs_id,
            "inputs": self.inputs,
        }
        if self.outputs:
            evaluation_dict["outputs"] = self.outputs
        if self.request_id:
            evaluation_dict["request_id"] = self.request_id
        if self.targets:
            evaluation_dict["targets"] = self.targets
        if self.assessments:
            evaluation_dict["assessments"] = [assess.to_dictionary() for assess in self.assessments]
        if self.metrics:
            evaluation_dict["metrics"] = [metric.to_dictionary() for metric in self.metrics]
        if self.error_code:
            evaluation_dict["error_code"] = self.error_code
        if self.error_message:
            evaluation_dict["error_message"] = self.error_message
        return evaluation_dict

    @classmethod
    def from_dictionary(cls, evaluation_dict: Dict[str, Any]):
        """
        Create an Evaluation object from a dictionary.

        Args:
            evaluation_dict (dict): Dictionary containing evaluation information.

        Returns:
            Evaluation: The Evaluation object created from the dictionary.
        """
        evaluation_id = evaluation_dict["evaluation_id"]
        run_id = evaluation_dict["run_id"]
        inputs_id = evaluation_dict["inputs_id"]
        inputs = evaluation_dict["inputs"]
        outputs = evaluation_dict.get("outputs")
        request_id = evaluation_dict.get("request_id")
        targets = evaluation_dict.get("targets")
        assessments = None
        if "assessments" in evaluation_dict:
            assessments = [
                Assessment.from_dictionary(assess) for assess in evaluation_dict["assessments"]
            ]
        metrics = None
        if "metrics" in evaluation_dict:
            metrics = [Metric.from_dictionary(metric) for metric in evaluation_dict["metrics"]]
        error_code = evaluation_dict.get("error_code")
        error_message = evaluation_dict.get("error_message")
        return cls(
            evaluation_id=evaluation_id,
            run_id=run_id,
            inputs_id=inputs_id,
            inputs=inputs,
            outputs=outputs,
            request_id=request_id,
            targets=targets,
            assessments=assessments,
            metrics=metrics,
            error_code=error_code,
            error_message=error_message,
        )
